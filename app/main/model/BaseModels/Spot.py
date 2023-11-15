import os
from dataclasses import dataclass

from model.BaseModels.BaseSerializedModel import BaseModel


@dataclass
class Spot(BaseModel):
    visible: bool
    mine: bool
    value: int
    flagged: bool
    DEBUG = True

    def __init__(self, is_mine=False):

        self.mine = is_mine
        self.value = 0
        self.visible = False
        self.flagged = False

    def __repr__(self):

        if os.getenv("DEBUG") == "True":
            return f"{'v' if self.visible else '-'}{'M' if self.mine else '-' }{self.value}{'F' if self.flagged else '-' } "
        if not self.visible:
            return "◼"
        if self.mine:
            return "⁎"
        if self.flagged:
            return "F"
        return str(self.value)
