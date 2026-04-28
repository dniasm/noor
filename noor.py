import requests
import json

def chat(message):
    url="http://localhost:11434/api/generate"

    data = {
        "model" : "mistral",
        "prompt" : message,
        "stream" : False
    }

    response = requests.post(url, json=data)
    return json.loads(response.text)["response"]

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    response = chat(user_input)
    print(f"Noor: {response}\n")
