import os
from dotenv import load_dotenv

load_dotenv()

LANGS = ['cpp', 'python', 'java', 'cs', 'html', 'css', 'js', 'json', 'xml', 'swift', 'php']

APP_URL = os.getenv('APP_URL', 'https://paste.geekclass.ru')
SIMILARITY_LEVEL = int(os.getenv('SIMILARITY_LEVEL', 75))
MAX_SIMILAR_CODES = int(os.getenv('MAX_SIMILAR_CODES', 8))
CONNECTION_STRING = os.getenv('CONNECTION_STRING', 'postgresql+psycopg2://username:password@localhost:5432/mydatabase')
CELERY_BROKER = os.getenv('CELERY_BROKER', 'redis://localhost:6379/0')
DEBUG = bool(os.getenv('DEBUG', False))
PORT = int(os.getenv('PORT', 8084))
SECRET = os.getenv('SECRET', 'key')
AUTH_URL = os.getenv('AUTH_URL', 'https://codingprojects.ru/insider/jwt?redirect_url=')
JWT_SECRET = os.getenv('JWT_SECRET')
SUBMIT_URL = os.getenv('SUBMIT_URL')

GPT_MODEL = os.getenv('GPT_MODEL', 'gpt-4o-mini')
GPT_KEY = os.getenv('GPT_KEY')
GPT_GATEWAY = os.getenv('GPT_GATEWAY', 'https://gpt-gateway.ai.medsenger.ru/ask')
