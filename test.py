import mysql.connector

# Configuration de la connexion
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "yanis",  # Mets ton mot de passe ici
    "database": "sprint_data"
}

try:
    conn = mysql.connector.connect(**db_config)
    print("✅ Connexion réussie à MySQL")
    conn.close()
except mysql.connector.Error as err:
    print(f"❌ Erreur : {err}")
