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
- cryptography

## Install
## Install

```bash
pip install -r requirements.txt
```

## Usage

1. Put the file you want to encrypt in the project folder (or use full path).
2. Run:

```bash
python main.py
```

3. Choose:
- `1` to encrypt
- `2` to decrypt

## Example

### Encrypt
- Option: `1`
- File path: `notes.txt`
- Password: `mypassword123`

### Decrypt
- Option: `2`
- File path: `notes.txt`
- Password: `mypassword123`

## Warning 

If you forget the password, you cannot recover the encrypted file.
