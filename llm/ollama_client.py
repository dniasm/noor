import json
import os
import requests

OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://localhost:11343")

def generate_reply(prompt):
    response = requests.post(
        f"{OLLAMA_HOST}/api/generate",
        json = {
            "model" : "mistral",
            "prompt" : prompt,
            "stream" : False
        }
    )
    reply = json.loads(response.text)["response"]
    return reply