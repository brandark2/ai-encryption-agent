import os
from cryptography.fernet import Fernet
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Générer une clé
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

WATCH_FOLDER = "./data"

def encrypt_file(filepath):
    with open(filepath, "rb") as f:
        data = f.read()

    encrypted = cipher.encrypt(data)

    with open(filepath + ".enc", "wb") as f:
        f.write(encrypted)

    print(f"Fichier chiffré : {filepath}")

class MonitorHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            encrypt_file(event.src_path)

if __name__ == "__main__":
    print("Agent IA actif...")
    
    if not os.path.exists(WATCH_FOLDER):
        os.makedirs(WATCH_FOLDER)

    observer = Observer()
    observer.schedule(MonitorHandler(), WATCH_FOLDER, recursive=False)
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()

    observer.join()