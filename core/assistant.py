from memory.history_store import append_exchange, load_history, save_history
from memory.vector_store import get_relevant_context, add_exchange
from llm.prompts import system
from llm.ollama_client import generate_reply

conversation_history = load_history()

def chat(message):
    append_exchange(conversation_history, "user", message)

    relevant_context = get_relevant_context(message)

    full_prompt = f"System: {system}\n"

    if relevant_context:
        full_prompt += "Relevant context from earlier conversations:\n"
        for past_query, past_reponse in relevant_context:
            full_prompt += f"User previously asked: {past_query}\n Noor previously replied {past_reponse}\n"
        full_prompt += "\n"

    for entry in conversation_history[-6:]:
        if entry["role"] == "user":
            full_prompt += f"User: {entry['content']}\n"
        else:
            full_prompt += f"Noor: {entry['content']}\n"
    
    reply = generate_reply(full_prompt)
    append_exchange(conversation_history, "assistant", reply)

    add_exchange(message, reply)

    return reply

def save():
    save_history(conversation_history)