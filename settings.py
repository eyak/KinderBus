from dotenv import load_dotenv
import os
BASE_DIR = os.path.dirname(__file__)

load_dotenv(dotenv_path=os.path.join(BASE_DIR, '.env'))

AIRTABLE_API_KEY = os.environ['AIRTABLE_API_KEY']
AIRTABLE_BUS_BASE_ID = os.environ['AIRTABLE_BUS_BASE_ID'] 
