# LeakDNA

LeakDNA is a file integrity and data leak attribution system designed to detect tampering and trace the origin of leaked files.

Unlike traditional integrity checkers, LeakDNA not only identifies whether a file has been modified but also attempts to determine the source of the leak using embedded markers.

---

## Core Idea

Every file is treated as a traceable entity:

- Generate a unique fingerprint using SHA-256 hashing  
- Embed a hidden identity marker into the file  
- Store metadata for tracking  
- Verify integrity and extract origin during analysis  

---

## Features

- File fingerprinting using SHA-256  
- Detection of unauthorized file modifications  
- Leak source identification via embedded markers  
- System-level user identification (no manual input dependency)  
- CLI-based workflow  
- JSON-based persistent storage  

---

## Project Structure


LeakDNA/
├── core/
│ ├── hash_engine.py
│ └── watermark.py
├── utils/
│ └── file_handler.py
├── data/
│ └── hashes.json
└── main.py


---

## Usage

### Add a File


python3 main.py add <file_path>


- Generates hash  
- Embeds marker  
- Stores metadata  

---

### Verify a File


python3 main.py verify <file_path>


- Recomputes hash  
- Detects modification  
- Extracts leak source  

---

## Example


echo "confidential data" > test.txt
python3 main.py add test.txt

echo "tampered" >> test.txt

python3 main.py verify test.txt


Output:


File has been MODIFIED
Leak source identified: <system_user>


---

## Tech Stack

- Python 3  
- SHA-256 (hashlib)  
- JSON (data storage)  
- Linux / CLI  

---

## Limitations

- Marker is visible and can be removed  
- No encryption or tamper resistance yet  
- Works only on local system  
- Not resistant to advanced adversaries  

---

## Future Improvements

- Encrypted watermarking  
- Binary/steganographic embedding  
- Cryptographic signatures  
- Cloud-based tracking  
- Real-time monitoring and alerts  

---

## Why This Project

Most systems stop at integrity verification.

LeakDNA extends this by introducing attribution, allowing tracking of where a file originated rather than only detecting that it changed.

---

## Author

ISHRIT
