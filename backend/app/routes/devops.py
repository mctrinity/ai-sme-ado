import httpx
from fastapi import APIRouter, HTTPException
from dotenv import load_dotenv
import os
import base64  # Needed for manual basic auth encoding

# Load environment variables
# load_dotenv()
load_dotenv(override=True)  # 🔥 Force reload of environment variables


# Azure DevOps Configuration
AZURE_ORG = os.getenv("AZURE_DEVOPS_ORG")
AZURE_PROJECT = os.getenv("AZURE_DEVOPS_PROJECT")
AZURE_PAT = os.getenv("AZURE_DEVOPS_PAT")

# Debug
print(AZURE_ORG)
print(AZURE_PROJECT)
print(AZURE_PAT)

# Debugging logs
print("DEBUG: AZURE_ORG =", os.getenv("AZURE_DEVOPS_ORG"))
print("DEBUG: AZURE_PROJECT =", os.getenv("AZURE_DEVOPS_PROJECT"))
print("DEBUG: AZURE_PAT =", os.getenv("AZURE_DEVOPS_PAT"))

if not AZURE_ORG or not AZURE_PROJECT or not AZURE_PAT:
    raise ValueError("Missing required environment variables: AZURE_DEVOPS_ORG, AZURE_DEVOPS_PROJECT, or AZURE_DEVOPS_PAT")

# API Router
router = APIRouter()

# Encode PAT for Basic Auth
auth_token = base64.b64encode(f":{AZURE_PAT}".encode()).decode()

# Headers for authentication
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Basic {auth_token}"
}

@router.get("/repos")
def get_repositories():
    """Fetch all repositories from Azure DevOps."""
    url = f"https://dev.azure.com/{AZURE_ORG}/_apis/git/repositories?api-version=6.0"
    
    try:
        response = httpx.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
    except httpx.RequestError as exc:
        raise HTTPException(status_code=500, detail=f"Error contacting Azure DevOps: {str(exc)}")
    except httpx.HTTPStatusError as exc:
        raise HTTPException(status_code=exc.response.status_code, detail=f"Azure DevOps API error: {exc.response.text}")
    
    return response.json()

@router.get("/pipelines")
def get_pipelines():
    """Fetch all pipelines from Azure DevOps."""
    url = f"https://dev.azure.com/{AZURE_ORG}/{AZURE_PROJECT}/_apis/pipelines?api-version=6.0"
    
    try:
        response = httpx.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
    except httpx.RequestError as exc:
        raise HTTPException(status_code=500, detail=f"Error contacting Azure DevOps: {str(exc)}")
    except httpx.HTTPStatusError as exc:
        raise HTTPException(status_code=exc.response.status_code, detail=f"Azure DevOps API error: {exc.response.text}")
    
    return response.json()