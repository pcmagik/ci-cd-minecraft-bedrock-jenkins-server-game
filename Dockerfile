# Używamy najnowszej wersji Ubuntu jako bazowego obrazu
FROM ubuntu:latest

# Instalacja wymaganych narzędzi (np. wget, unzip, curl)
RUN apt-get update && apt-get install -y wget unzip curl libcurl4

# Utworzenie katalogu dla serwera Minecraft Bedrock
WORKDIR /opt/minecraft/bedrock

# Skopiowanie pobranego pliku bedrock-server.zip do obrazu
COPY bedrock-server.zip .

# Rozpakowanie serwera Bedrock i usunięcie pliku .zip
RUN unzip bedrock-server.zip && rm bedrock-server.zip

# Akceptacja licencji (w tym przypadku nie jest wymagana eula.txt, ale dodajemy to jako dobry przykład)
RUN echo "eula=true" > eula.txt

# Otwarcie portu Minecraft Bedrock
EXPOSE 19132/udp

# Uruchomienie serwera
CMD ["LD_LIBRARY_PATH=.", "./bedrock_server"]
