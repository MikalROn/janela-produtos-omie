import os
from py_dotenv import read_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
read_dotenv(dotenv_path)

API_KEY = os.getenv('API_KEY').strip()
API_SECREET = os.getenv('API_SECREET').strip()