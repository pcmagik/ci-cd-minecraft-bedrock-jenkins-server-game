from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Konfiguracja Selenium do uruchamiania w trybie headless
options = Options()
options.headless = True
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Otwórz stronę pobierania Minecraft Bedrock
driver.get("https://www.minecraft.net/en-us/download/server/bedrock")

# Kliknij przycisk akceptacji warunków
accept_button = driver.find_element(By.XPATH, "//a[contains(text(), 'I Agree')]")
accept_button.click()

# Znajdź i pobierz link do serwera
download_button = driver.find_element(By.XPATH, "//a[contains(@href, 'bedrock-server')]")
server_url = download_button.get_attribute('href')

# Pobierz plik
driver.get(server_url)

# Zamknij przeglądarkę
driver.quit()
