from selenium import webdriver
from selenium.webdriver.common.by import By
import requests  # Assure-toi d'importer requests

# Initialiser le driver (ici avec Chrome)
driver = webdriver.Chrome()

# Ouvrir la page web
driver.get("https://www.podcastics.com/podcast/episode/le-marketing-sportif-grand-gagnant-de-lia-2-313767/")

# Attendre que la page se charge complètement
driver.implicitly_wait(10)

# Trouver le lien de téléchargement par sa classe CSS
download_link = driver.find_element(By.CSS_SELECTOR, 'div.websitePodcastHeaderLinkDownloadText a')

# Extraire l'URL du lien de téléchargement
download_url = download_link.get_attribute('href')

# Afficher l'URL
print(f"URL de téléchargement : {download_url}")

# Ajouter des en-têtes pour imiter une requête de navigateur
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0',
    'Referer': "https://www.podcastics.com/",  # Optionnel, mais peut aider
}

# Télécharger le fichier avec requests
response = requests.get(download_url, headers=headers)  # Utiliser les en-têtes ici
if response.status_code == 200:
    with open('podcast_episode.mp3', 'wb') as f:
        f.write(response.content)
    print("Téléchargement réussi : podcast_episode.mp3")
else:
    print(f"Erreur lors du téléchargement : {response.status_code}")

# Fermer le driver
driver.quit()
