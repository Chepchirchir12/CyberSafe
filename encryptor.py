from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode
import os

def generate_key(password: str, salt: bytes):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = urlsafe_b64encode(kdf.derive(password.encode()))
    return key

def encrypt_file(file_path, password):
    salt = os.urandom(16)
    key = generate_key(password, salt)
    cipher = Fernet(key)

    with open(file_path, "rb") as file:
        data = file.read()

    encrypted_data = cipher.encrypt(data)

    with open(file_path, "wb") as file:
        file.write(salt + encrypted_data)

def decrypt_file(file_path, password):
    with open(file_path, "rb") as file:
        file_data = file.read()

    salt = file_data[:16]
    encrypted_data = file_data[16:]

    key = generate_key(password, salt)
    cipher = Fernet(key)

    decrypted_data = cipher.decrypt(encrypted_data)

    with open(file_path, "wb") as file:
        file.write(decrypted_data)
