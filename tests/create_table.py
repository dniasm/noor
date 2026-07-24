import os
import psycopg2
from dotenv import load_dotenv

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
cursor.execute("""                
                CREATE TABLE conversation_memory(
                    id SERIAL PRIMARY KEY,
                    user_query TEXT NOT NULL,
                    assistant_response TEXT NOT NULL,
                    query_embedding VECTOR(768),
                    response_embedding VECTOR(768),
                    created_at TIMESTAMP DEFAULT NOW()
                )
""")

conn.commit()

cursor.close()
conn.close()
