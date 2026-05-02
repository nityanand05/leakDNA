from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os

from core.hash_engine import generate_hash
from core.watermark import embed_marker, extract_marker
from utils.file_handeler import load_db, save_db

WATCH_DIR = "watched_folder"

class Handler(FileSystemEventHandler):

    def on_created(self, event):
        if event.is_directory:
            return

        file_path = event.src_path
        print(f"[+] New file detected: {file_path}")

        db = load_db()

        import getpass
        user = getpass.getuser()

        embed_marker(file_path, user)
        file_hash = generate_hash(file_path)

        db[file_path] = {
            "hash": file_hash,
            "owner": user
        }

        save_db(db)
        print(f"[+] File tracked: {file_path}")

    def on_modified(self, event):
        if event.is_directory:
            return

        file_path = event.src_path
        db = load_db()

        if file_path not in db:
            return

        current_hash = generate_hash(file_path)

        if db[file_path]["hash"] != current_hash:
            print(f"[!] File modified: {file_path}")

            marker = extract_marker(file_path)

            if marker:
                print(f"[+] Leak source: {marker}")
            else:
                print(f"[!] Marker removed, last known owner: {db[file_path]['owner']}")

observer = Observer()
observer.schedule(Handler(), WATCH_DIR, recursive=False)
observer.start()

print(f"[*] Monitoring folder: {WATCH_DIR}")

try:
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    observer.stop()

observer.join()