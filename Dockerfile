FROM python:3.14.0b1-bookworm

RUN apt update && apt upgrade
RUN apt install -y portaudio19-dev
RUN pip install pyaudio
RUN apt install -y pipewire-alsa

RUN useradd -m -d /home/app app
USER app

WORKDIR /home/app/contacter

CMD ["python3", "main.py"]
