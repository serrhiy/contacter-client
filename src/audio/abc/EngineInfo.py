"""
This file defines api interface to retrieve
information about audio engine.

All implementations must necessarily implement this
interface, and users must rely only on the methods
defined here.
"""

import abc
import enum

class FormatType(enum.Enum):
  float32 = enum.auto()
  int32 = enum.auto()
  int16 = enum.auto()
  int8 = enum.auto()
  uInt8 = enum.auto()

class State(enum.Enum):
  abort = enum.auto()    # Error ocurred, stop playback/recording
  complete = enum.auto() # This was the last block of audio data
  contin = enum.auto()   # There is more audio data to come

class ErrorType(enum.Enum):
  inputOverflow = enum.auto()
  inputUnderflow = enum.auto()
  noDevice = enum.auto()
  outputOverflow = enum.auto()
  outputUnderflow = enum.auto()

class EngineInfo(abc.ABC):

  @staticmethod
  @abc.abstractmethod
  def get_engine_info() -> str:
    """
    Returns the info of the underlying audio backend.

    Example: PortAudio V19.6.0-devel
    """
    message = 'The class has not defined a static method get_engine_info'
    raise NotImplementedError(message)

  @staticmethod
  @abc.abstractmethod
  def get_engine_code() -> int:
    """
    Returns the info of the underlying audio backend.

    Example: 1246720
    """
    message = 'The class has not defined a static get_engine_code'
    raise NotImplementedError(message)
