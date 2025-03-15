import pandas as pd

# 1. Charger les données avec le bon séparateur et encodage
def charger_donnees(fichier):
    try:
        df = pd.read_csv(fichier, sep=";", encoding="utf-8")
        print("Données chargées avec succès ! ")
        return df
    except Exception as e:
        print(f" Erreur lors du chargement des données : {e}")
        return None

# 2. Nettoyer les données
def nettoyer_donnees(df):
    if df is None or df.empty:
        print("Aucune donnée à nettoyer. ")
        return None

    # Correction des colonnes numériques (Prix, Taxes)
    colonnes_prix = ["Prix", "Price (excl. tax)", "Price (incl. tax)", "Tax"]
    for col in colonnes_prix:
        df[col] = df[col].str.replace("Â£", "").astype(float)

    print("Données nettoyées avec succès ! ")
    return df

# 3. Analyser les données
def analyser_donnees(df):
    if df is None or df.empty:
        print("Aucune donnée à analyser. ")
        return

    print("\n **Analyse des données** \n")
    
    # Nombre total de livres
    print(f" Nombre total de livres : {len(df)}")
    
    # Prix moyen des livres
    print(f" Prix moyen : £{df['Prix'].mean():.2f}")
    
    # Nombre de livres en stock
    en_stock = df[df["Disponibilité"] == "In stock"]
    print(f" Livres en stock : {len(en_stock)}")

    # Distribution des étoiles
    print("\n Distribution des notes :")
    print(df["Étoiles"].value_counts())

# 4. Sauvegarder les données nettoyées
def sauvegarder_donnees(df, fichier_sortie):
    if df is None or df.empty:
        print("Aucune donnée à sauvegarder. ")
        return
    
    df.to_csv(fichier_sortie, sep=";", encoding="utf-8", index=False)
    print(f"Données sauvegardées dans {fichier_sortie} ")

# 5. Exécution du programme
if __name__ == "__main__":
    fichier_entree = "books_toscrape.csv"  # Remplace par ton fichier CSV
    fichier_sortie = "livres_nettoyes.csv"

    df = charger_donnees(fichier_entree)
    df = nettoyer_donnees(df)
    analyser_donnees(df)
    sauvegarder_donnees(df, fichier_sortie)
