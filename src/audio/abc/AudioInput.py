"""
This file defines interface for audio input devices.

All implementations must necessarily implement this
interface, and users must rely only on the methods
defined here.
"""

import abc

class AudioInput(abc.ABC):
  @abc.abstractmethod
  def close(self): pass

  @abc.abstractmethod
  def get_available(self) -> int: pass

  @abc.abstractmethod
  def is_active(self) -> bool: pass

  @abc.abstractmethod
  def is_stopped(self) -> bool: pass

  @abc.abstractmethod
  def read(self, num_frames: int, exception_on_overflow = True) -> bytes: pass

  @abc.abstractmethod
  def start_stream(self): pass

  @abc.abstractmethod
  def stop_stream(self): pass
