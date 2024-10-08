from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()


url = "https://www.podcastics.com/podcast/episode/le-marketing-sportif-grand-gagnant-de-lia-2-313767/"

driver.get(url)


try:

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "fa-check")))
    element.click()
    
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "websitePodcastHeaderLinkMore")))
    element.click()

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Téléchargez")))
    element.click()

    time.sleep(1000)

finally:
    driver.quit()