import os
import time
import logging
from cryptography.fernet import Fernet
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configuration
WATCHED_FOLDER = "files_to_encrypt"
KEY_FILE = "secret.key"

# Logging
logging.basicConfig(
    filename="encryption.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Gestion de la clé
def load_or_create_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as f:
            key = f.read()
        logging.info("Clé chargée depuis le fichier")
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
        logging.info("Nouvelle clé générée et sauvegardée")
    return key

key = load_or_create_key()
cipher = Fernet(key)

# Préparation du dossier
if not os.path.exists(WATCHED_FOLDER):
    os.makedirs(WATCHED_FOLDER)
    logging.info(f"Dossier créé : {WATCHED_FOLDER}")

print(f"Surveillance du dossier : {WATCHED_FOLDER}")

# Chiffrement
def encrypt_file(filepath):
    try:
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
        print(f"Chiffré : {filepath}")

    except Exception as e:
        logging.error(f"Erreur chiffrement {filepath} : {e}")
        print(f"Erreur : {e}")

# Déchiffrement
def decrypt_file(filepath):
    try:
        if not filepath.endswith(".encrypted"):
            return

        with open(filepath, "rb") as file:
            data = file.read()

        decrypted_data = cipher.decrypt(data)
        original_path = filepath.replace(".encrypted", "")

        with open(original_path, "wb") as file:
            file.write(decrypted_data)

        os.remove(filepath)

        logging.info(f"Fichier déchiffré : {filepath}")
        print(f"Déchiffré : {filepath}")

    except Exception as e:
        logging.error(f"Erreur déchiffrement {filepath} : {e}")
        print(f"Erreur : {e}")

# Gestionnaire d’événements
class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            logging.info(f"Nouveau fichier : {event.src_path}")
            encrypt_file(event.src_path)

# Lancement
if __name__ == "__main__":
    observer = Observer()
    event_handler = FileHandler()
    observer.schedule(event_handler, WATCHED_FOLDER, recursive=False)

    observer.start()
    print("Agent lancé (chiffrement automatique)")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Arrêt de l’agent")

    observer.join()
