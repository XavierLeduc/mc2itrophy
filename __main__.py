from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
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
driver.get("https://www.podcastics.com/podcast/mc2i-podcasts/")

driver.set_window_size(1920, 1080)

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "websitePodcastEntryContentTitle")))

    podcasts = driver.find_elements(By.CLASS_NAME, "websitePodcastEntryContentTitle")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "fa-check"))).click()
    print("Cookies acceptés.")
    for i in range(len(podcasts)):
        podcasts = driver.find_elements(By.CLASS_NAME, "websitePodcastEntryContentTitle")
        print("URL actuelle : ", driver.current_url)
        podcast = podcasts[i]
        podcast_title = podcast.text
        print("Podcast: ", podcast_title)

        link = podcast.find_element(By.TAG_NAME, "a")
        driver.execute_script("arguments[0].click();", link)
        print("URL actuelle : ", driver.current_url)





        driver.save_screenshot(podcast_title + ".png")

        locations = ["ID", "LINK_TEXT"]
        elements = ["websitePodcastHeaderLinkMore", "Download"]

        for location, element in zip(locations, elements):
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((getattr(By, location), element))).click()
            driver.save_screenshot(element + ".png")

        driver.save_screenshot("fin_dl.png")
        time.sleep(1)
        driver.back()
        driver.refresh()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "websitePodcastEntryContentTitle")))
        print("URL actuelle : ", driver.current_url)
        driver.save_screenshot("retour_accueil.png")

        podcasts = driver.find_elements(By.CLASS_NAME, "websitePodcastEntryContentTitle")

finally:
    driver.quit()

if os.path.exists(download_dir):
    print("Téléchargement terminé et fichier disponible.")
else:
    print("Téléchargement échoué ou chemin incorrect.")
