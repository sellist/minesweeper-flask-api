from dataclasses import dataclass

from model.BaseModels.BaseSerializedModel import BaseModel


@dataclass
class GameConfig(BaseModel):
    width: int
    height: int
    mines: int
    playing: bool
    won: bool
    lost: bool

    def __init__(self, width, height, mines):
        self.width = width
        self.height = height
        self.mines = mines
        self.playing = False
        self.won = False
        self.lost = False

    @classmethod
    def from_tuple(cls, tup):
        return cls(tup[0], tup[1], tup[2])
