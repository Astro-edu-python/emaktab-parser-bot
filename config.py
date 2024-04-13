import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).parent
load_dotenv(BASE_DIR / '.env')


EMAKTAB_LOGIN = os.environ.get('EMAKTAB_LOGIN')
EMAKTAB_PASSWORD = os.environ.get('EMAKTAB_PASSWORD')
BOT_TOKEN = os.environ.get('BOT_TOKEN')
