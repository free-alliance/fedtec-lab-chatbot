from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import httpx
from fastapi.middleware.cors import CORSMiddleware
import re
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from langChain_chat_model import get_chat_response

load_dotenv()

LANGFLOW_TOKEN = os.getenv("LANGFLOW_TOKEN")

app = FastAPI()

# Allow frontend on port 5173
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://sf.courts.ca.gov/"],  # Or ["*"] for all origins (not recommended for prod)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/fedtec-lab/health")
async def health_check():
    return {"status": "ok"}



class ChatRequest(BaseModel):
    input_value: str

@app.post("/fedtec-lab/chatbot")
async def chat_endpoint(chat_req: ChatRequest):
    reply = get_chat_response(chat_req.input_value)
    return {"response": reply}

