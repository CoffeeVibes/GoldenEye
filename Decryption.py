from cryptography.fernet import Fernet

def decrypt_message(encrypted_message: bytes, key: bytes) -> str:

    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message)
    
    return decrypted_message.decode()