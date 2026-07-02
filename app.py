from fastapi import FastAPI
from main import main
from models import Message,ChatRequest
from langchain_core.messages import ToolMessage
import uvicorn 
import os
import json

PORT = int(os.environ.get("PORT", 8000))
app = FastAPI()

@app.get("/")
def func():
    return {"message": "server is runnning"}

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
if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=PORT,
        reload=True
    )