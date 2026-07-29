import json
import requests

def generate_reply(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json = {
            "model" : "mistral",
            "prompt" : prompt,
            "stream" : False
        }
    )
    reply = json.loads(response.text)["response"]
    return reply