import os
from cryptography.fernet import Fernet
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import logging

# -------------------------------
# 🔐 Configuration du logging
# -------------------------------
logging.basicConfig(
    filename="encryption.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -------------------------------
# 🔑 Génération de la clé
# -------------------------------
key = Fernet.generate_key()
cipher = Fernet(key)

# Dossier à surveiller
WATCHED_FOLDER = "files_to_encrypt"

# Création du dossier s’il n’existe pas
if not os.path.exists(WATCHED_FOLDER):
    os.makedirs(WATCHED_FOLDER)
    logging.info(f"Dossier créé : {WATCHED_FOLDER}")

print(f"📂 Surveillance du dossier : {WATCHED_FOLDER}")

# -------------------------------
# 🔐 Fonction de chiffrement
# -------------------------------
def encrypt_file(filepath):
    try:
        # Vérifier si déjà chiffré
        if filepath.endswith(".encrypted"):
            return

        with open(filepath, "rb") as file:
            data = file.read()

        encrypted_data = cipher.encrypt(data)

        encrypted_path = filepath + ".encrypted"

        with open(encrypted_path, "wb") as file:
            file.write(encrypted_data)

        os.remove(filepath)

        logging.info(f"Fichier chiffré : {filepath}")
        print(f"✅ Fichier chiffré : {filepath}")

    except Exception as e:
        logging.error(f"Erreur avec {filepath} : {e}")
        print(f"❌ Erreur : {e}")

# -------------------------------
# 👀 Gestionnaire d’événements
# -------------------------------
class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            logging.info(f"Nouveau fichier détecté : {event.src_path}")
            encrypt_file(event.src_path)

# -------------------------------
# 🚀 Lancement de l’agent
# -------------------------------
if __name__ == "__main__":
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCHED_FOLDER, recursive=False)

    observer.start()
    print("🚀 Agent de chiffrement lancé...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("🛑 Arrêt de l'agent")

    observer.join()
