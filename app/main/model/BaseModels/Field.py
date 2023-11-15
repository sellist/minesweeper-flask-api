from dataclasses import dataclass

from model.BaseModels.BaseSerializedModel import BaseModel
from model.BaseModels.Spot import Spot


@dataclass
class Field(BaseModel):
    field: list[list[Spot]]

    @property
    def width(self):
        return len(self.field[0])

    @property
    def height(self):
        return len(self.field)

    @property
    def visible_spaces(self):
        count = 0
        for x in self.field:
            for y in x:
                if y.visible:
                    count += 1

        return count

    @property
    def total_spaces(self):
        return len(self.field) * len(self.field[0])

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.field])
