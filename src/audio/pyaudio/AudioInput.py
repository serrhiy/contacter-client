"""
This file defines interface for audio input devices.

All implementations must necessarily implement this
interface, and users must rely only on the methods
defined here.
"""

from audio import abc
from pyaudio import PyAudio
from audio.abc.EngineInfo import FormatType
from audio.abc import EngineInfo

class AudioInput(abc.AudioInput):
  def __init__(self, audio: PyAudio, rate: float, channels: int, format: FormatType,
               device_index: int, frames_per_buffer: int,
               start = True):
    frmt = EngineInfo.get_sample_size(format)
    self.stream = audio.open(rate, channels, frmt, True, False, device_index, None, frames_per_buffer, start, None, None, None)

  def close(self):
    self.stream.close()

  def get_available(self) -> int:
    return self.stream.get_read_available()

  def is_active(self) -> bool:
    return self.stream.is_active()

  def is_stopped(self) -> bool:
    return self.stream.is_stopped()

  def read(self, num_frames: int, exception_on_overflow = True) -> bytes:
    return self.stream.read(num_frames, exception_on_overflow)

  def start_stream(self):
    self.stream.start_stream()

  def stop_stream(self):
    self.stream.stop_stream()
