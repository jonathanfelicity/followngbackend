from dotenv import load_dotenv
load_dotenv()

import os

BASE_URL = '/api/v1'

DBURI = os.getenv('DBURI')
SECRET_KEY = os.getenv('SECRET_KEY')





