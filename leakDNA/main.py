import sys
from core.hash_engine import generate_hash
from utils.file_handeler import load_db, save_db

def add_file(file_path):
    db = load_db()
    file_hash = generate_hash(file_path)

    if file_hash is None:
        print("❌ File not found")
        return

    db[file_path] = file_hash
    save_db(db)

    print(f"✅ File added with hash: {file_hash}")

def verify_file(file_path):
    db = load_db()
    file_hash = generate_hash(file_path)

    if file_path not in db:
        print("⚠️ File not tracked")
        return

    if db[file_path] == file_hash:
        print("✅ File is ORIGINAL")
    else:
        print("🚨 File has been MODIFIED")

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