# Access API Key Generation

This project provides functionality to generate and manage API keys using Django.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Shahid-Sheimi/access_api_key_generation
   cd access_api_key_generation
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
## install reqs
pip install -r requirements.txt
## generate fernet
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"

## .env
SECRET_KEY="your_django_secret_key"
DEBUG=True  # Set to False in production
FERNET_KEY="your_generated_fernet_key"
## migrate comamands
python manage.py migrate
## runserver 
python manage.py runserver
