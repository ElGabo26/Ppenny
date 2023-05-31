from dotenv import load_dotenv
import os

# Carga las variables de entorno desde el archivo .env
load_dotenv()

def env():
    env_vars = {
        'DB_HOST': os.getenv('DB_HOST'),
        'DB_PASS': os.getenv('DB_PASS'),
        'DB_USER': os.getenv('DB_USER'),
        'DB_DATABASE': os.getenv('DB_DATABASE')
    }
    return env_vars

