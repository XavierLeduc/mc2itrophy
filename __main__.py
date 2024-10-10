from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os

download_dir = "/home/downloads"
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

chrome_prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
chrome_options.add_experimental_option("prefs", chrome_prefs)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.podcastics.com/podcast/episode/le-marketing-sportif-grand-gagnant-de-lia-2-313767/")

try:
    locations = ["CLASS_NAME", "ID", "LINK_TEXT"]
    elements = ["fa-check", "websitePodcastHeaderLinkMore", "Download"]

    for location, element in zip(locations, elements):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((getattr(By, location), element))).click()
        driver.save_screenshot(element + ".png")
    
    time.sleep(120)

finally:
    driver.quit()

if os.path.exists(download_dir):
    print("Téléchargement terminé et fichier disponible.")
else:
    print("Téléchargement échoué ou chemin incorrect.")
