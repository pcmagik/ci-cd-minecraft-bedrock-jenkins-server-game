from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Konfiguracja Selenium do uruchamiania w trybie headless
options = Options()
options.add_argument("--headless")  # Tryb bez interfejsu graficznego
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Otwórz stronę pobierania Minecraft Bedrock
    driver.get("https://www.minecraft.net/en-us/download/server/bedrock")

    # Poczekaj chwilę, aby upewnić się, że strona się załadowała
    time.sleep(5)

    # Kliknij przycisk akceptacji warunków, jeśli jest dostępny
    try:
        accept_button = driver.find_element(By.XPATH, "//a[contains(text(), 'I Agree')]")
        accept_button.click()
        time.sleep(2)  # Poczekaj chwilę na załadowanie strony po kliknięciu
    except Exception as e:
        print("Przycisk akceptacji nie znaleziony, być może nie jest wymagany: ", e)

    # Znajdź link do serwera i pobierz URL
    download_button = driver.find_element(By.XPATH, "//a[contains(@href, 'bedrock-server')]")
    server_url = download_button.get_attribute('href')

    # Wyświetl link do konsoli
    print(f"Link do pobrania serwera: {server_url}")

finally:
    # Zamknij przeglądarkę
    driver.quit()
