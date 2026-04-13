from fastapi import FastAPI
from pydantic import BaseModel
from app.core.agent import run_agent

app = FastAPI(title="Smart Customer Support API")


class ChatRequest(BaseModel):
    message: str

@app.get("/")
def read_root():
    return {"message": "Akıllı Müşteri Destek API Çalışıyor!"}

@app.post("/chat")
def chat_endpoint(request: ChatRequest):
    """Kullanıcı mesajını alır, ajana iletir ve cevabı döner."""
    agent_response = run_agent(request.message)
    return {"response": agent_response}