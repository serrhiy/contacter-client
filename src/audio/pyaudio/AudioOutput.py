"""
This file defines interface for audio output devices.

All implementations must necessarily implement this
interface, and users must rely only on the methods
defined here.
"""

from audio import abc
from pyaudio import Stream

class AudioOutput(abc.AudioOutput):
  def __init__(self, stream: Stream):
    super().__init__()
    self.stream = stream

  def close(self):
    self.stream.close()

  def get_available(self) -> int:
    return self.stream.get_read_available()

  def is_active(self) -> bool:
    return self.stream.is_active()

  def is_stopped(self) -> bool:
    return self.stream.is_stopped()

  def write(self, frames: bytes, num_frames=None, fail_on_underflow=False) -> bytes:
    self.stream.write(frames, num_frames, fail_on_underflow)

  def start_stream(self):
    self.stream.start_stream()

  def stop_stream(self):
    self.stream.stop_stream()
