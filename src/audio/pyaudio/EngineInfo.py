import pyaudio
from audio import abc

class EngineInfo(abc.EngineInfo):

  @staticmethod
  def get_engine_info() -> str:
    return pyaudio.get_portaudio_version_text()

  @staticmethod
  def get_engine_code() -> str:
    return pyaudio.get_portaudio_version()
