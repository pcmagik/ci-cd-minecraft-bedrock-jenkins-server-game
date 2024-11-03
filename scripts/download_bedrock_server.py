from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode for automation

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Open the Minecraft Bedrock download page
    driver.get("https://www.minecraft.net/en-us/download/server/bedrock")

    # Wait for the page to load
    time.sleep(5)

    # Click the acceptance button if available
    try:
        accept_button = driver.find_element(By.XPATH, "//a[contains(text(), 'I Agree')]")
        accept_button.click()
        time.sleep(2)  # Wait for the page to load after clicking
    except Exception as e:
        print("Acceptance button not found, it might not be required: ", e)

    # Find the server download link and get the URL
    download_button = driver.find_element(By.XPATH, "//a[contains(@href, 'bedrock-server')]")
    server_url = download_button.get_attribute('href')

    # Print the download link to the console
    print(f"Server download link: {server_url}")

except Exception as e:
    print("An error occurred: ", e)

finally:
    # Close the browser
    driver.quit()
