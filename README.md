Sprint Data Project

Description

Sprint Data Project est une application Python permettant d'extraire, nettoyer, analyser et stocker des données à partir de sources externes. Ce projet utilise Selenium pour le scraping, Pandas pour le nettoyage, Matplotlib pour la visualisation et MySQL pour le stockage des données.

Structure du Projet

sprint_data_project/
│── data/                           # Dossier pour stocker les fichiers de données
│   ├── raw_data.csv                # Données brutes extraites
│   ├── cleaned_data.csv             # Données nettoyées
│
│── database/                        # Dossier pour la gestion de la base de données
│   ├── schema.sql                    # Script de création de la base MySQL
│   ├── insert_data.sql                # Script d'insertion des données
│
│── src/                             # Dossier contenant les scripts Python
│   ├── scraper.py                   # Script pour extraire les données
│   ├── database_manager.py           # Gestion de la base de données (connexion, insertion)
│   ├── data_cleaning.py              # Nettoyage des données avec Pandas
│   ├── analysis.py                   # Analyse et visualisation des données
│
│── notebooks/                        # Jupyter notebooks pour exploration des données
│   ├── data_exploration.ipynb        # Notebook pour tester et explorer les données
│
│── reports/                         # Dossier pour les livrables
│   ├── presentation.pdf              # Présentation finale en PDF
│
│── requirements.txt                  # Liste des dépendances Python
│── README.md                         # Instructions pour exécuter le projet
│── config.py                         # Fichier de configuration (base de données, URL, etc.)
│── main.py                           # Script principal orchestrant tout le projet

Installation

1. Cloner le projet

git clone https://github.com/ton_repo/sprint_data_project.git
cd sprint_data_project

2. Installer les dépendances

Assurez-vous d'avoir Python 3 installé, puis exécutez :

pip install -r requirements.txt

3. Configurer la base de données

Assurez-vous d'avoir MySQL installé et en cours d'exécution.

Exécutez les scripts SQL pour créer et remplir la base de données :

mysql -u root -p < database/schema.sql
mysql -u root -p < database/insert_data.sql

Vérifiez que la configuration de la base de données est correcte dans config.py.

Utilisation

1. Scraper les données

python src/scraper.py

Les données brutes seront enregistrées dans data/raw_data.csv.

2. Nettoyer les données

python src/data_cleaning.py

Les données nettoyées seront stockées dans data/cleaned_data.csv.

3. Analyser les données

python src/analysis.py

Les résultats et les visualisations seront générés dans reports/.

4. Exécuter le projet complet

python main.py

Dépannage

Erreur liée à Selenium et ChromeDriver

Si vous obtenez l'erreur :

selenium.common.exceptions.WebDriverException: Message: unknown error: DevToolsActivePort file doesn't exist

Essayez d'installer ou de mettre à jour ChromeDriver :

sudo apt update && sudo apt install chromium-chromedriver

Ajoutez ensuite le chemin du driver dans votre config.py :

CHROMEDRIVER_PATH = "/usr/bin/chromedriver"

Contribution

Si vous souhaitez contribuer, n'hésitez pas à ouvrir une issue ou une pull request sur GitHub.