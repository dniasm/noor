from fastapi import FastAPI
from pydantic import BaseModel
from core.assistant import chat

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat_endpoint(request : ChatRequest):
    reply = chat(request.message)
    return{"reply" : reply}

@app.get("/health")
def health_check():
    return{"status" : "okay"}