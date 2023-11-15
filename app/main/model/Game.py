from dataclasses import dataclass

from model.BaseModels.Field import Field
from model.BaseModels.GameConfig import GameConfig
from model.BaseModels.SecondarySerializedModel import SecondaryModel


@dataclass
class Game(SecondaryModel):
    board: Field
    config: GameConfig

    def __init__(self, board, config):
        self.config = config
        self.board = board
