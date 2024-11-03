FROM ubuntu:latest

# Instalacja zależności
RUN apt-get update && apt-get install -y wget unzip python3 python3-pip

# Instalacja Selenium i innych zależności Python
RUN pip3 install selenium requests

# Utwórz katalog dla serwera
WORKDIR /opt/minecraft/bedrock

# Skopiuj skrypt pobierający serwer do obrazu
COPY scripts/download_bedrock_server.py /opt/minecraft/bedrock/

# Uruchom skrypt do pobierania najnowszej wersji Minecraft Bedrock Server
RUN python3 download_bedrock_server.py

# Rozpakuj serwer
RUN unzip bedrock-server.zip && rm bedrock-server.zip

# Otwórz port Minecraft Bedrock
EXPOSE 19132/udp

# Start serwera
CMD ["./bedrock_server"]
