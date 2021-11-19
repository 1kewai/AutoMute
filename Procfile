docker container rm -f AutoMute
docker container run -it -d --name AutoMute --restart=always ubuntu_server bash
docker exec rythm apt update
docker exec rythm apt install python3-pip ffmpeg wget -y
docker exec rythm pip3 install discord
docker cp AutoMute.py AutoMute:/AutoMute.py
docker cp auth.py AutoMute:/auth.py
docker exec -d AutoMute python3 /AutoMute.py
