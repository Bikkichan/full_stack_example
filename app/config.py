import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

uri = os.getenv('DATABASE_URL')

#if uri.startswith("postgres://"):
#    uri = uri.replace("postgres://", "postgresql://", 1)

DATABASE_URL = uri

print(uri)

conn = psycopg2.connect(DATABASE_URL)
