import json
from django.core.management.utils import get_random_secret_key  
from dotenv import load_dotenv
import os

load_dotenv()

user_name = os.getenv('POSTGRES_USER')
password = os.getenv('POSTGRES_PASSWORD')
db_user_name = os.getenv('POSTGRES_USER')
db_name = os.getenv('POSTGRES_DB')
host = os.getenv('POSTGRES_HOST')

with open('core/config.json', 'w', encoding='utf-8') as f:
    json.dump({'DB_USER':db_user_name, 'DB_PASSWORD':password,
     'DB_NAME':db_name, 'DB_HOST':host, 'SECRET_KEY':get_random_secret_key()}, f, ensure_ascii=False, indent=4)