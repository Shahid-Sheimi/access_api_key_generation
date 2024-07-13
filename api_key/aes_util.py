# api_key/aes_util.py
import base64
from cryptography.fernet import Fernet
from django.conf import settings

FERNET_ENCRYPT_KEY = settings.FERNET_ENCRYPT_KEY

def encrypt_value(value):
    if value:
        value = str(value)
        fernet_key = Fernet(key=FERNET_ENCRYPT_KEY)
        encrypted_value = fernet_key.encrypt(value.encode("utf-8"))
        encrypted_value = base64.urlsafe_b64encode(encrypted_value).decode("utf-8")
        return encrypted_value

def decrypt_value(value):
    if value:
        value = base64.urlsafe_b64decode(value)
        fernet_key = Fernet(key=FERNET_ENCRYPT_KEY)
        decrypted_value = fernet_key.decrypt(value).decode("utf-8")
        return decrypted_value
