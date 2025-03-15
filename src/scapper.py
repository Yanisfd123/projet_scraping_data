import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de base pour accéder aux différentes pages
BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

# Headers pour éviter d'être bloqué par le site
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

# Conversion des étoiles en notation numérique
STAR_RATINGS = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

# Dictionnaire pour stocker les données des livres
books = {
    "Titre": [],
    "Prix": [],
    "Disponibilité": [],
    "Étoiles": [],
    "Price (excl. tax)": [],
    "Price (incl. tax)": [],
    "Tax": []
}

# Limite du nombre de pages à scraper
max_pages = 30

# Parcourir les pages une par une
for page in range(1, max_pages + 1):
    url = BASE_URL.format(page)
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"Problème d'accès à la page {page}, arrêt du scraping.")
        break  # Si une page ne charge pas, on ne continue pas

    soup = BeautifulSoup(response.text, 'html.parser')

    # Récupérer tous les livres affichés sur la page
    items = soup.find_all("article", class_="product_pod")

    if not items:
        print(f"Arrêt du scraping : seulement {page - 1} pages trouvées.")
        break  # Si aucune donnée trouvée, inutile de continuer

    for item in items:
        try:
            title = item.find("h3").find("a")["title"]
            price = item.find("p", class_="price_color").text.strip()
            availability = item.find("p", class_="instock availability").text.strip()

            # Récupération des étoiles (notation de 1 à 5)
            star_class = item.find("p", class_="star-rating")["class"]
            star_rating = STAR_RATINGS.get(star_class[1], 0)  # Si pas trouvé, on met 0

            # Accéder à la page du produit pour récupérer les prix détaillés
            product_link = "https://books.toscrape.com/catalogue/" + item.find("h3").find("a")["href"]
            product_response = requests.get(product_link, headers=HEADERS)
            product_soup = BeautifulSoup(product_response.text, "html.parser")

            price_excl_tax = product_soup.find("th", string="Price (excl. tax)").find_next("td").text.strip()
            price_incl_tax = product_soup.find("th", string="Price (incl. tax)").find_next("td").text.strip()
            tax = product_soup.find("th", string="Tax").find_next("td").text.strip()

            # Ajouter les données extraites dans le dictionnaire
            books["Titre"].append(title)
            books["Prix"].append(price)
            books["Disponibilité"].append(availability)
            books["Étoiles"].append(star_rating)
            books["Price (excl. tax)"].append(price_excl_tax)
            books["Price (incl. tax)"].append(price_incl_tax)
            books["Tax"].append(tax)

        except Exception as e:
            print(f"Erreur lors de l'extraction d'un livre : {e}")
            continue

# Enregistrement des données dans un fichier CSV
df = pd.DataFrame(books)
df.to_csv("../data/raw_data.csv", index=False, encoding='utf-8', sep=";")

print("Scraping terminé ! Données enregistrées dans raw_data.csv")