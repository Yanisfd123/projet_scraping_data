import mysql.connector
import pandas as pd

# 🔧 Configuration de la base (modifiable via config.py)
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "yanis",  
    "database": "sprint_data"
}

# 📌 Fonction pour se connecter à MySQL
def connect_db():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        print("✅ Connexion réussie à MySQL")
        return conn
    except mysql.connector.Error as err:
        print(f"❌ Erreur de connexion : {err}")
        return None

# 📌 Fonction pour insérer des données
def insert_data_from_csv(csv_file):
    conn = connect_db()
    if not conn:
        return

    cursor = conn.cursor()
    df = pd.read_csv(csv_file, sep=";")

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO books (titre, prix, disponibilite, etoiles, price_excl_tax, price_incl_tax, tax)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, tuple(row))

    conn.commit()
    print(f"📂 {len(df)} livres insérés dans la base de données")
    cursor.close()
    conn.close()

if __name__ == "__main__":
    insert_data_from_csv("../src/livres_nettoyes.csv")
