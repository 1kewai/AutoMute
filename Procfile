docker container rm -f AutoMute
docker container run -it -d --name AutoMute --restart=always --cpus=0.25 --memory=0.25g ubuntu_server bash
docker exec AutoMute apt update
docker exec AutoMute apt install python3-pip ffmpeg wget -y
docker exec AutoMute pip3 install discord
docker cp AutoMute.py AutoMute:/AutoMute.py
docker cp auth.py AutoMute:/auth.py
docker exec -d AutoMute python3 /AutoMute.py
