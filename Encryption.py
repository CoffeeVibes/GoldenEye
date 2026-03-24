from cryptography.fernet import Fernet

def encrypt_message(message: str, key: bytes) -> bytes:

    fernet = Fernet(key)
    return fernet.encrypt(message.encode())
