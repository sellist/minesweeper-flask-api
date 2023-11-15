import logging
from dataclasses import dataclass

from model.BaseModels.GameConfig import GameConfig
from model.BaseModels.SecondarySerializedModel import SecondaryModel


@dataclass
class BeginRequest(SecondaryModel):
    width: int
    height: int
    mines: int
    config: GameConfig

    def __init__(self, d: dict):
        if d is not None:
            for key, value in d.items():
                try:
                    setattr(self, key, value)
                except AttributeError:
                    logging.warning(f"Error parsing json to {__class__} init. key: {key} val: {value}")
        self.config = self.to_config()

    def to_config(self):
        return GameConfig.from_tuple((self.width, self.height, self.mines))
