import sys
import os
from fastapi import FastAPI

# Add 'backend' to Python's module search path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/backend")

from app.routes.devops import router as devops_router  # Import DevOps API routes

app = FastAPI()

# Register router with correct prefix
app.include_router(devops_router, prefix="/devops")  # ✅ This is correct

@app.get("/")
def root():
    return {"message": "AI SME for Azure DevOps is running!"}
