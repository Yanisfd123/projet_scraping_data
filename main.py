from src.data_cleaning import nettoyer_donnees
from database.database_manager import insert_data_from_csv

def main():
    print("🚀 Démarrage du projet Sprint Data")
    
    # Étape 1 : Nettoyage des données
    fichier_entree = "src/books_toscrape.csv"
    fichier_sortie = "src/livres_nettoyes.csv"
    
    df = nettoyer_donnees(fichier_entree)
    if df is not None:
        df.to_csv(fichier_sortie, sep=";", encoding="utf-8", index=False)
        print("✅ Données nettoyées et sauvegardées")

    # Étape 2 : Insertion des données en base
    insert_data_from_csv(fichier_sortie)

if __name__ == "__main__":
    main()
