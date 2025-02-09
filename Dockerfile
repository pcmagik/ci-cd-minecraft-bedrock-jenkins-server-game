# Używamy najnowszej wersji Ubuntu jako bazowego obrazu
FROM ubuntu:latest

# Instalacja wymaganych narzędzi (np. wget, unzip, curl, oraz wymagane biblioteki)
RUN apt-get update && apt-get install -y wget unzip curl libcurl4 libssl3

# Utworzenie katalogu dla serwera Minecraft Bedrock
WORKDIR /opt/minecraft/bedrock

# Skopiowanie pobranego pliku bedrock-server.zip do obrazu
COPY bedrock-server.zip .

# Rozpakowanie serwera Bedrock i usunięcie pliku .zip
RUN unzip -o bedrock-server.zip && \
    rm bedrock-server.zip

# Kopiowanie i ustawienie uprawnień dla server.properties
COPY server.properties .
RUN chmod 644 server.properties

# Weryfikacja zawartości pliku server.properties
RUN grep "gamemode=creative" server.properties && \
    grep "force-gamemode=true" server.properties && \
    grep "allow-cheats=true" server.properties

# Nadanie uprawnień wykonywania plikowi serwera
RUN chmod +x bedrock_server

# Akceptacja licencji (w tym przypadku nie jest wymagana eula.txt, ale dodajemy to jako dobry przykład)
RUN echo "eula=true" > eula.txt

# Otwarcie portu Minecraft Bedrock
EXPOSE 19132/udp

# Ustawienie zmiennej środowiskowej i uruchomienie serwera
CMD ["./bedrock_server"]
