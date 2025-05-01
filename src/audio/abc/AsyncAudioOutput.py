"""
This file defines interface for async audio output devices.

All implementations must necessarily implement this
interface, and users must rely only on the methods
defined here.
"""

import abc
from audio.abc.EngineInfo import State
from audio.abc import AudioOutput 

class AsyncAudioOutput(AudioOutput):
  # @abc.abstractmethod
  # async def write(data: bytes, state: State): pass

  @abc.abstractmethod
  def write(data: bytes, state: State): pass
