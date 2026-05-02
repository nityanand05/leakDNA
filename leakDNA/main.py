import sys
import getpass
from core.watermark import embed_marker, extract_marker
from core.hash_engine import generate_hash
from utils.file_handeler import load_db, save_db

def add_file(file_path):
    db = load_db()

    user_id = getpass.getuser()

    embed_marker(file_path, user_id)
    file_hash = generate_hash(file_path)
    print(file_hash)
    if file_hash is None:
        print("❌ File not found")
        return

    db[file_path] = {
        "hash": file_hash,
        "owner": user_id
    }

    save_db(db)

    print(f"✅ File tracked for user: {user_id}")

def verify_file(file_path):
    db = load_db()
    file_hash = generate_hash(file_path)
    print(file_hash)

    if file_path not in db:
        print("⚠️ File not tracked")
        return

    marker = extract_marker(file_path)

    if db[file_path]["hash"] == file_hash:
        print("✅ File is ORIGINAL")
    else:
        print("🚨 File has been MODIFIED")

        if marker:
            print(f"🕵️ Leak source identified: {marker}")
        else:
            print("❌ No marker found")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 main.py [add|verify] <file>")
        sys.exit()

    action = sys.argv[1]
    file_path = sys.argv[2]

    if action == "add":
        add_file(file_path)
    elif action == "verify":
        verify_file(file_path)
    else:
        print("❌ Invalid command")#/home/ishrit/Desktop/projects/leakDNA/