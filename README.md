# CyberSafe 

A secure file encryption and decryption tool built with Python.

## Features
- Encrypt any file with a password
- Decrypt encrypted files with the same password
- Uses PBKDF2 (SHA-256) for key derivation
- Uses Fernet symmetric encryption
- Random salt per file (stored inside the encrypted file)

## Requirements
- Python 3.9+
- `cryptography`

## Install
```bash
pip install -r requirements.txt
## Usage

1. Put the file you want to encrypt in the project folder (or use full path).
2. Run:

```bash
python main.py

---

###  Important
Make sure the triple backticks (```) are included exactly like above — that’s what makes the code block formatting work.

---

After pasting:

1. Click **Preview** at the top of the README editor  
   (to confirm formatting looks clean)
2. Click **Commit changes…**
3. Commit message:
