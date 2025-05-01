import os
import importlib
from audio import abc
from Config import Config
from audio.abc.EngineInfo import FormatType
import asyncio

config_path = os.path.join(os.path.dirname(__file__), 'config.json')

CHUNK = 1024

async def main():
  config = Config.file(config_path)
  module: abc = importlib.import_module(f'audio.{config.implementation}')
  engine_info = module.EngineInfo.get_engine_info()
  engine_code = module.EngineInfo.get_engine_code()
  print(engine_code, engine_info)
  with module.AudioDriver() as driver:
    idi = driver.get_default_input_device_info().index
    odi = driver.get_default_output_device_info().index
    rate = driver.get_default_input_device_info().default_sample_rate
    input_stream = driver.open_input_async_stream(rate, 2, FormatType.int16, idi, CHUNK)
    output_stream = driver.open_output_async_stream(rate, 2, FormatType.int16, odi, CHUNK)
    async for chunk in input_stream:
      output_stream.write(chunk)
    input_stream.close()
    output_stream.close()

if __name__ == '__main__':
  asyncio.run(main())
