from queue import Queue
import pyaudio
from audio import abc
from audio.abc.EngineInfo import State, FormatType
from .AudioOutput import AudioOutput

class AsyncAudioOutput(AudioOutput):
  def __init__(self, audio: pyaudio.PyAudio, rate: float, channels: int, format: FormatType,
               device_index: int, frames_per_buffer: int, start = True):
    self.queue = Queue()
    frmt = abc.EngineInfo.get_sample_size(format)
    def callback(input: bytes, frames: int, time: dict, status: int):
      return self.queue.get(), pyaudio.paContinue
    self.stream = audio.open(rate, channels, frmt, False, True, None,
                             device_index, frames_per_buffer, start, None, None, callback)
    
  def write(self, data: bytes, state: State = None):
    self.queue.put_nowait(data)
