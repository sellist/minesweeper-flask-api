__all__ = [
    "validate_config"
]

import os
from textwrap import dedent

from model.BaseModels.Spot import Spot
from model.Game import Game


def validate_config(data: Game):
    if None in {data.config.height, data.config.width, data.config.mines}:
        raise InvalidConfigException(f"None passed in as config parameter! {data.config.to_json()}")

    if data.board.width != data.config.width:
        raise InvalidConfigException(dedent(f"Width in config does not match actual board. Board: {data.board.width},"
                                            f"Config: {data.config.width}"))
    if data.board.height != data.config.height:
        raise InvalidConfigException(dedent(f"Height in config does not match actual board. Board: {data.board.height},"
                                            f"Config: {data.config.height}"))

    if data.board.height < int(os.getenv('MIN_HEIGHT')):
        raise InvalidConfigException(
            f"Invalid height entered in config {data.board.height} (Below minimum of {os.getenv('MIN_HEIGHT')}")

    if data.board.height > int(os.getenv('MAX_HEIGHT')):
        raise InvalidConfigException(
            f"Invalid height entered in config {data.board.height} (Above max of {os.getenv('MAX_HEIGHT')}")

    if data.board.width < int(os.getenv('MIN_WIDTH')):
        raise InvalidConfigException(
            f"Invalid width entered in config {data.board.width} (Below minimum of {os.getenv('MIN_WIDTH')}")

    if data.board.width > int(os.getenv('MAX_WIDTH')):
        raise InvalidConfigException(
            f"Invalid width entered in config {data.board.width} (Above max of {os.getenv('MAX_WIDTH')}")

    if data.config.mines > data.config.width * data.config.height:
        raise InvalidConfigException(
            f"Too many mines! {data.config.mines} vs max of {data.config.width * data.config.height}")

    count = 0
    board = data.board.field
    for x in board:
        y: Spot
        for y in x:
            if y.mine:
                count += 1

    if count != data.config.mines:
        raise InvalidConfigException(dedent(f"Mines in config does not match actual board. Board: {count},"
                                            f"Config: {data.config.mines}"))


def validate_move(x: int, y: int, game: Game):
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(game, Game):
        raise ValueError

    if 0 > x > game.board.width or 0 > y > game.board.height:
        raise OutOfBoundsException


class AlreadyFlaggedException(Exception):
    def __init__(self, message="Spot is already flagged"):
        super().__init__(message)


class OutOfBoundsException(Exception):
    def __init__(self, message="Spot is out of bounds"):
        super().__init__(message)


class InvalidInputException(Exception):
    def __init__(self, message="Input is not readable"):
        super().__init__(message)


class AlreadyVisibleException(Exception):
    def __init__(self, message="Spot is already visible"):
        super().__init__(message)


class InvalidConfigException(Exception):
    def __init__(self, message="Mismatch between board and configuration!"):
        super().__init__(message)
