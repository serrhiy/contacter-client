from audio.abc.EngineInfo import CallbackStatus, FormatType
from audio.abc import EngineInfo
from pyaudio import PyAudio
from queue import Queue
import asyncio
import pyaudio
from audio.pyaudio.AudioInput import AudioInput

class AsyncAudioInput(AudioInput):

  def __init__(self, audio: PyAudio, rate: float, channels: int, format: FormatType,
               device_index: int, frames_per_buffer: int, start = True):
    frmt = EngineInfo.get_sample_size(format)
    self.futures: Queue[asyncio.Future] = Queue()
    self.buffer = Queue()
    self.loop = asyncio.get_running_loop()
    def callback(input: bytes, frames: int, time: dict, status: int):
      if self.futures.qsize() > 0:
        future = self.futures.get_nowait()
        self.loop.call_soon_threadsafe(lambda: future.set_result(input))
      else:
        self.buffer.put_nowait(input)
      return None, pyaudio.paContinue
    self.stream = audio.open(rate, channels, frmt, True, False, device_index, None, frames_per_buffer, start, None, None, callback)

  def __aiter__(self) -> "AsyncAudioInput":
    return self

  def __anext__(self) -> tuple[bytes, int, CallbackStatus]:
    future = self.loop.create_future()
    if self.buffer.qsize() > 0: future.set_result(self.buffer.get_nowait())
    else: self.futures.put_nowait(future)
    return future
