import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("MYSQL_DATABASE_URL")
