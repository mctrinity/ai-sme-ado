import sys
import os
from fastapi import FastAPI

# Add 'backend' to Python's module search path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/backend")

from app.routes.devops import router as devops_router  # Import DevOps API routes
from app.routes.chatbot import router as chatbot_router  # ✅ Import Chatbot API

app = FastAPI()

# Register routers
app.include_router(devops_router, prefix="/devops")
app.include_router(chatbot_router, prefix="/chatbot")  # ✅ Register chatbot

@app.get("/")
def root():
    return {"message": "AI SME for Azure DevOps is running!"}
