import os
import importlib
from audio import abc
from Config import Config

config_path = os.path.join(os.path.dirname(__file__), 'config.json')

def main():
  config = Config.file(config_path)
  module: abc = importlib.import_module(f'audio.{config.implementation}')
  engine_info = module.EngineInfo.get_engine_info()
  engine_code = module.EngineInfo.get_engine_code()
  print(engine_code, engine_info)

if __name__ == '__main__': main()
