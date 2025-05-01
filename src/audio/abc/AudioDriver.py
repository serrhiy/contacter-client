"""
This file defines interface for audio driver.

All implementations must necessarily implement this
interface, and users must rely only on the methods
defined here.
"""

import abc
from dataclasses import dataclass
from audio.abc.EngineInfo import FormatType
from audio.abc import AudioInput, AudioOutput

@dataclass
class DeviceInfo:
  index: int
  name: str
  max_input_channels: int
  max_output_channels: int
  default_sample_rate: int

class AudioDriver(abc.ABC):

  @abc.abstractmethod
  def get_device_count(self) -> int:
    pass

  @abc.abstractmethod
  def is_input_format_supported(self, rate: int, device_index: int,
                                channels: int, format: FormatType) -> bool:
    pass

  @abc.abstractmethod
  def is_output_format_supported(self, rate: int, device_index: int,
                                 channels: int, format: FormatType) -> bool:
    pass

  @abc.abstractmethod
  def get_default_input_device_info(self) -> DeviceInfo:
    pass

  @abc.abstractmethod
  def get_default_output_device_info(self) -> DeviceInfo:
    pass

  @abc.abstractmethod
  def get_device_info_by_index(self, index: int) -> DeviceInfo:
    pass

  @abc.abstractmethod
  def __enter__(self) -> "AudioDriver": pass
  
  @abc.abstractmethod
  def __exit__(self, exc_type, exc_value, traceback): pass

  @abc.abstractmethod
  def open_input_stream(self, rate: float, channels: int, format: FormatType,
                        device_index: int, frames_per_buffer: int, start = True,
                        stream_callback = None) -> AudioInput: pass

  @abc.abstractmethod
  def open_output_stream(self, rate: float, channels: int, format: FormatType,
                         device_index: int, frames_per_buffer: int, start = True,
                         stream_callback = None) -> AudioOutput: pass
