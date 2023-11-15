import random

from model.BaseModels.Field import Field
from model.BaseModels.GameConfig import GameConfig
from model.BaseModels.Spot import Spot


def generate_board(config: GameConfig) -> Field:
    field = [[Spot() for _ in range(config.height)] for _ in range(config.width)]
    mines = random.sample(range(config.width * config.height), config.mines)

    for mine in mines:
        row = mine // config.height
        col = mine % config.height
        field[row][col] = Spot(True)
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if (0 <= r < config.width) and (0 <= c < config.height) and not field[r][c].mine:
                    field[r][c].value += 1

    return Field(field)


def _unpack_config(config: GameConfig) -> tuple[int, int, int]:
    return config.width, config.height, config.mines
