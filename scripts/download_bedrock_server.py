import requests
from bs4 import BeautifulSoup
import re
import time

# Definiowanie URL strony do pobrania Bedrock Servera
url = "https://www.minecraft.net/pl-pl/download/server/bedrock"

# Nagłówki, aby symulować przeglądarkę
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Funkcja do wielokrotnego pobierania strony w przypadku błędów
def get_response_with_retries(url, headers, retries=5, delay=5):
    for i in range(retries):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                return response
            else:
                print(f"Błąd pobierania strony. Kod odpowiedzi: {response.status_code}. Próba {i+1} z {retries}.")
        except requests.exceptions.RequestException as e:
            print(f"Błąd połączenia: {e}. Próba {i+1} z {retries}.")
        time.sleep(delay)
    return None

# Pobieranie strony z linkiem do serwera Bedrock
print("Pobieranie strony z linkiem do serwera Bedrock...")
response = get_response_with_retries(url, headers)

if not response:
    print("Nie udało się pobrać strony po maksymalnej liczbie prób.")
    exit(1)

# Przetwarzanie HTML za pomocą BeautifulSoup
data = response.text
soup = BeautifulSoup(data, 'html.parser')

# Wyszukiwanie linku do pobrania pliku z serwerem Bedrock
print("Wyszukiwanie linku do pobrania...")
download_link = None
for a_tag in soup.find_all('a', href=True):
    if re.search(r'bedrock-server-.*?\.zip', a_tag['href']):
        download_link = a_tag['href']
        break

if not download_link:
    print("Nie znaleziono linku do pobrania Bedrock Servera.")
    exit(1)

# Uzupełnienie linku do pobrania, jeśli jest względny
if download_link.startswith('/'):
    download_link = f"https://www.minecraft.net{download_link}"

# Pobieranie pliku serwera
file_name = download_link.split('/')[-1]
print(f"Pobieranie pliku {file_name}...")
file_response = get_response_with_retries(download_link, headers)

if file_response and file_response.status_code == 200:
    with open("bedrock-server.zip", 'wb') as file:
        file.write(file_response.content)
    print(f"Pomyślnie pobrano plik {file_name}")
else:
    print(f"Błąd pobierania pliku po maksymalnej liczbie prób.")
    exit(1)
