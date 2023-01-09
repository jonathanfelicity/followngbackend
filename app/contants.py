from dotenv import load_dotenv
load_dotenv()

import os

BASE_URL = '/api/v1'

DBURI ='postgresql://username:password@hostname/database_name'
os.getenv("ACCESS_KEY")




