import pyaudio
from audio import abc
from audio.abc.EngineInfo import FormatType
from audio.abc.AudioDriver import DeviceInfo
from .AudioInput import AudioInput
from .AudioOutput import AudioOutput
from .AsyncAudioInput import AsyncAudioInput
from .AsyncAudioOutput import AsyncAudioOutput

def to_device_info(audio_device_info: dict[str: str|int|float]) -> DeviceInfo:
  index = audio_device_info['index']
  name = audio_device_info['name']
  input_channels = audio_device_info['maxInputChannels']
  output_channels = audio_device_info['maxOutputChannels']
  sample_rate = int(audio_device_info['defaultSampleRate'])
  return DeviceInfo(index, name, input_channels, output_channels, sample_rate)

class AudioDriver(abc.AudioDriver):

  def __init__(self):
    super().__init__()
    self.audio = pyaudio.PyAudio()

  def get_device_count(self) -> int:
    return self.audio.get_device_count()

  def is_input_format_supported(self, rate: int, device_index: int,
                                channels: int, format: FormatType) -> bool:
    frmt = abc.EngineInfo.get_sample_size(format)
    return self.audio.is_format_supported(rate, device_index, channels, frmt)

  def is_output_format_supported(self, rate: int, device_index: int,
                                 channels: int, format: FormatType) -> bool:
    frmt = abc.EngineInfo.get_sample_size(format)
    return self.audio.is_format_supported(rate, None, None, None, 
                                          device_index, channels, frmt)

  def get_default_input_device_info(self) -> DeviceInfo:
    info = self.audio.get_default_input_device_info()
    return to_device_info(info)

  def get_default_output_device_info(self) -> DeviceInfo:
    info = self.audio.get_default_output_device_info()
    return to_device_info(info)

  def get_device_info_by_index(self, index: int) -> DeviceInfo:
    info = self.audio.get_device_info_by_index(index)
    return to_device_info(info)

  def __enter__(self):
    self.__init__()
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    self.audio.terminate()

  def open_input_stream(self, rate: float, channels: int, format: FormatType,
               device_index: int, frames_per_buffer: int,
               start = True) -> abc.AudioInput:
    return AudioInput(self.audio, rate, channels, format, device_index, frames_per_buffer, start)

  def open_output_stream(self, rate: float, channels: int, format: FormatType,
               device_index: int, frames_per_buffer: int,
               start = True) -> abc.AudioOutput:
    return AudioOutput(self.audio, rate, channels, format, device_index, frames_per_buffer, start)
  
  def open_input_async_stream(self, rate: float, channels: int, format: FormatType,
              device_index: int, frames_per_buffer: int,
              start = True) -> abc.AsyncAudioInput:
    return AsyncAudioInput(self.audio, rate, channels, format, device_index, frames_per_buffer, start)

  def open_output_async_stream(self, rate: float, channels: int, format: FormatType,
                device_index: int, frames_per_buffer: int,
                start = True) -> abc.AsyncAudioOutput:
    return AsyncAudioOutput(self.audio, rate, channels, format, device_index, frames_per_buffer, start)
