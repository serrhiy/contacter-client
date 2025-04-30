import json
from typing import Any

class Config:

  def __init__(self, content: dict[str: Any]):
    for key, value in content.items():
      data = value if type(value) != dict else Config(value)
      setattr(self, key, data)

  @staticmethod
  def file(path) -> "Config":
    with open(path) as file:
      content = json.load(file)
      return Config(content)

  def get_dict(self) -> dict[str, Any]:
    result = dict()
    for key, value in self.__dict__.items():
      result[key] = value if type(value) != Config else value.get_dict()
    return result

  def __str__(self):
    return str(self.get_dict())
