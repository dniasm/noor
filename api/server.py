from fastapi import FastAPI
from pydantic import BaseModel
from core.assistant import chat
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat_endpoint(request : ChatRequest):
    reply = chat(request.message)
    return{"reply" : reply}

@app.get("/health")
def health_check():
    return{"status" : "okay"}