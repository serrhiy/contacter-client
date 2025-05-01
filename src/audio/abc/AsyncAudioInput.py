"""
This file defines interface for async audio input devices.

All implementations must necessarily implement this
interface, and users must rely only on the methods
defined here.
"""

from audio.abc.EngineInfo import CallbackStatus
from audio.abc.AudioInput import AudioInput
import abc

class AsyncAudioInput(AudioInput):
  @abc.abstractmethod
  def __aiter__(self) -> "AsyncAudioInput": pass

  @abc.abstractmethod
  def __anext__(self) -> tuple[bytes, int, CallbackStatus]: pass

