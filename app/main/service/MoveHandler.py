import logging

from model.BaseModels.Spot import Spot
from model.Game import Game


def place_move(x: int, y: int, game: Game) -> Game:
    try:
        validate_move(x, y, game)
    except Exception as e:
        logging.info(e)
        return game

    if game.board.field[y][x].visible:
        print("spot already visible")
        return game

    if game.board.field[y][x].mine:
        game.config.lost = True

    g = _flood_fill(x, y, game)

    if (game.board.total_spaces - game.board.visible_spaces) == game.config.mines:
        game.config.won = True
        game.config.playing = False
        return game

    return g


def validate_move(x: int, y: int, game: Game):
    spot: Spot = game.board.field[y][x]
    if spot.flagged:
        raise InvalidMoveException("Spot is flagged")


def _flood_fill(x: int, y: int, game: Game) -> Game:
    board = game.board.field
    if 0 <= y < len(board) and 0 <= x < len(board[0]) and board[y][x].mine is False and board[y][x].visible is False:
        adjacent_mines = 0

        # Count mines in adjacent cells
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if 0 <= y + dx < len(board) and 0 <= x + dy < len(board[0]) and board[y + dx][x + dy].mine:
                    adjacent_mines += 1

        if adjacent_mines == 0:
            board[y][x].visible = True
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    _flood_fill(x + dy, y + dx, game)
        else:
            board[y][x].visible = True
            board[y][x].value = adjacent_mines

    return game


class InvalidMoveException(Exception):
    def __init__(self, message="Mismatch between board and configuration!"):
        super().__init__(message)
