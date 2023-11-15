import logging

from model.BaseModels.GameConfig import GameConfig
from model.Game import Game
from model.dto.BeginRequest import BeginRequest
from service import MoveHandler
from service.board import validator, generator


def create_custom_config(x, y, mines) -> GameConfig:
    return GameConfig(x, y, mines)


def create_from_request(req: BeginRequest):
    return Game(create(req.config), req.config)


def create(config: GameConfig):
    return Game(generator.generate_board(config=config), config)


def start(x, y, game: Game):
    if not game.config.playing:
        while game.board.field[y][x].mine or game.board.field[y][x].value > 0:
            board = generator.generate_board(config=game.config)
            game = Game(board, game.config)

    try:
        validator.validate_config(game)
    except Exception as e:
        logging.info(e)
        return None

    MoveHandler.place_move(x, y, game)

    game.config.playing = True
    return game


def move(x, y, game):
    if not game.config.playing:
        return start(x, y, game)
    else:
        return MoveHandler.place_move(x, y, game)
