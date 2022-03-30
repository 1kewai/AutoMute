FROM ubuntu:22.04

RUN apt update
RUN apt upgrade -y
RUN apt install -y python3-pip ffmpeg wget
RUN pip3 install discord
COPY AutoMute.py AutoMute.py
COPY auth.py auth.py

CMD ["python3", "/AutoMute.py"]
