from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()
password = os.environ.get("DB_PASSWORD")

conn = psycopg2.connect(
    host = "localhost",
    port = 5432,
    dbname = "postgres",
    user = "postgres",
    password = password
)

cursor = conn.cursor()
cursor.execute("CREATE EXTENSION IF NOT EXISTS vector;")
conn.commit()

cursor.close()
conn.close()

print("Connected and Vector Extension Established")