"""
This file defines interface for audio output devices.

All implementations must necessarily implement this
interface, and users must rely only on the methods
defined here.
"""

import abc

class AudioOutput(abc.ABC):
  
  @abc.abstractmethod
  def close(self): pass

  @abc.abstractmethod
  def get_available(self) -> int: pass

  @abc.abstractmethod
  def is_active(self) -> bool: pass

  @abc.abstractmethod
  def is_stopped(self) -> bool: pass

  @abc.abstractmethod
  def write(self, frames, num_frames=None, exception_on_underflow=False) -> bytes: pass

  @abc.abstractmethod
  def start_stream(self): pass

  @abc.abstractmethod
  def stop_stream(self): pass
