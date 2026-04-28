import requests
import json

conversation_history = []

def chat(message):
    conversation_history.append({
        "role" : "user",
        "content" : message
    })

    full_prompt = ""

    for entry in conversation_history:
        if entry["role"] == "user":
            full_prompt += f"User: {entry['content']}\n"
        else:
            full_prompt += f"Noor: {entry['content']}\n"
    
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model" : "phi3:mini",
            "prompt" : full_prompt,
            "stream" : False
        }
    )

    reply = json.loads(response.text)["response"]
    conversation_history.append({
        "role" : "assistant",
        "content" : reply
    })

    return reply

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    response = chat(user_input)
    print(f"Noor: {response}\n")
