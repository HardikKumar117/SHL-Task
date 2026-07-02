from fastapi import FastAPI
from main import main
from models import Message,ChatRequest
from langchain_core.messages import ToolMessage
import json
app = FastAPI()

@app.get("/health")
def root():
    return {"status": "ok"}

@app.post("/chat")
def chat(request:ChatRequest):
    conv =str(request.messages)
    response=main(conv)
    tool_messages = [msg for msg in response["messages"] if isinstance(msg, ToolMessage)]

    return {"response": response["messages"][-1].content,
            "recommendations": json.loads( tool_messages[-1].content)}