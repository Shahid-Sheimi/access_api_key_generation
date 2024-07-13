# api_key/models.py
from django.db import models
from .aes_util import encrypt_value
from uuid import uuid4

class APIKey(models.Model):
    key = models.CharField(max_length=10, unique=True)  # Adjust max_length as needed

    @classmethod
    def generate_and_save(cls):
        new_token = 'nsol_' + str(uuid4())[:6]  
        encrypted_token = encrypt_value(new_token)
        api_key = cls.objects.create(key=encrypted_token)
        return api_key
