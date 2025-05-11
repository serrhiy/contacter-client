# How to run in Linux
```
git clone https://github.com/serrhiy/contacter-client.git
cd contacter-client
docker build -t pyaudio .
docker run --rm --privileged -e XDG_RUNTIME_DIR=/tmp -v /run/user/1000/pipewire-0:/tmp/pipewire-0 -v $(pwd)/src:/home/app/contacter pyaudio:latest
```
