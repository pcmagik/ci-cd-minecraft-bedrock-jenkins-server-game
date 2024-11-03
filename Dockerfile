FROM ubuntu:latest

# Instalacja zależności
RUN apt-get update && apt-get install -y wget unzip

# Utwórz katalog dla serwera
WORKDIR /opt/minecraft/bedrock

# Skopiuj pobrany plik serwera
COPY bedrock-server.zip .

# Rozpakuj serwer
RUN unzip bedrock-server.zip && rm bedrock-server.zip

# Akceptacja licencji (tworząc plik eula.txt lub coś podobnego, jeśli to wymagane)
RUN echo "eula=true" > eula.txt

# Otwórz port Minecraft Bedrock
EXPOSE 19132/udp

# Start serwera
CMD ["./bedrock_server"]
