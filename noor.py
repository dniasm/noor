from memory.history_store import load_history, save_history, append_exchange
from memory.vector_store import add_exchange, get_relevant_context
from llm.prompts import system
from llm.ollama_client import generate_reply
from core.assistant import chat, save

while True:
    user_input = input("You: ")
    if "quit" in user_input.strip().lower():
        save()
        print("Goodbye.")
        break
    response = chat(user_input)
    print(f"Noor: {response}\n")
