from enum import Enum

from model.BaseModels.GameConfig import GameConfig


class MineAmounts(Enum):
    EASY = GameConfig(10, 10, 10)
    MEDIUM = GameConfig(15, 15, 20)
    EXPERT = GameConfig(20, 30, 50)
