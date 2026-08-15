import requests
import os
from dotenv import load_dotenv
import psycopg2
from pgvector.psycopg2 import register_vector


load_dotenv()
password = os.environ.get("DB_PASSWORD")
db_host = os.environ.get("DB_HOST", "localhost")
ollama_host = os.environ.get("OLLAMA_HOST", "http://localhost:11434")

def get_embeddings(texts):
    response = requests.post(
        f"{ollama_host}/api/embed",
        json={
            "model" : "nomic-embed-text",
            "input" : texts
        }
    )
    return response.json()["embeddings"]

def get_connection():
    conn = psycopg2.connect(
        host = db_host,
        port = 5432,
        dbname = "postgres",
        user = "postgres",
        password = password
    )
    register_vector(conn)
    return conn

def add_exchange(user_query, assistant_response):
    embeddings = get_embeddings([user_query, assistant_response])
    query_embedding, response_embedding = embeddings

    if not is_valid_embedding(query_embedding) or not is_valid_embedding(response_embedding):
        embeddings = get_embeddings([user_query, assistant_response])
        query_embedding, response_embedding = embeddings

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO conversation_memory
        (user_query, assistant_response, query_embedding, response_embedding)
        VALUES (%s,%s,%s,%s)
        """,
        (user_query, assistant_response, query_embedding, response_embedding)
    )

    conn.commit()
    cursor.close()
    conn.close()

def get_relevant_context(message, top_k = 3):
    query_embedding = get_embeddings([message])[0]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT user_query, assistant_response
        FROM conversation_memory
        ORDER BY query_embedding <=> %s :: vector
        LIMIT %s;
        """,
        (query_embedding,top_k)
    )

    results = cursor.fetchall()
    cursor.close()
    conn.close()

    return results

def is_valid_embedding(vector , expected_dim = 768):
    if len(vector) != expected_dim:
        return False
    return any(value != 0 for value in vector)
