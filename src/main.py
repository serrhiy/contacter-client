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
  driver = module.AudioDriver()
  for index in range(driver.get_device_count()):
    info = driver.get_device_info_by_index(index)
    print(info, end='\n\n')

if __name__ == '__main__': main()
