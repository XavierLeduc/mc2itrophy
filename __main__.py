from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.podcastics.com/podcast/episode/le-marketing-sportif-grand-gagnant-de-lia-2-313767/")

try:

    locations = ["CLASS_NAME","ID","LINK_TEXT"]
    elements = ["fa-check","websitePodcastHeaderLinkMore","Téléchargez"]
    for location, element in zip(locations,elements):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((getattr(By, location), element))).click()
    
    time.sleep(1000)

finally:
    driver.quit()