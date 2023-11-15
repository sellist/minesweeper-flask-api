import json

from model.BaseModels.BaseSerializedModel import BaseModel


class SecondaryModel:
    def to_json(self):
        output = dict()
        for k, v in self.__dict__.items():
            if isinstance(v, BaseModel):
                d = json.loads(v.to_json())
                output[k] = d
            else:
                output[k] = v
        return output
