import json
import os

def load_history(path="memory.json"):
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return[]

def save_history(history, path="memory.json"):
    with open(path, "w") as f:
        json.dump(history, f, indent=2)

def append_exchange(history, role, content):
    entry = {"role" : role, "content" : content}
    history.append(entry)