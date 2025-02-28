import os
import openai
import time
import logging
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from dotenv import load_dotenv
from rich.console import Console

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("Missing OpenAI API Key!")

# Setup Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Define Request Model
class ChatRequest(BaseModel):
    user_query: str

# Initialize Router & Console
router = APIRouter()
console = Console()

@router.post("/chat")
async def ask_chatbot(request: ChatRequest):
    """Smart chatbot using GPT-3.5-Turbo with detailed responses, streaming, and logging."""
    try:
        client = openai.AsyncOpenAI(api_key=OPENAI_API_KEY)
        
        # Start timer for performance tracking
        start_time = time.time()

        async def generate():
            response = await client.chat.completions.create(
                model="gpt-3.5-turbo",  # ✅ Using GPT-3.5-Turbo for speed
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an Azure DevOps expert. Provide detailed, step-by-step instructions "
                            "with thorough explanations, best practices, common pitfalls, and alternative approaches."
                        )
                    },
                    {"role": "user", "content": request.user_query}
                ],
                stream=True,  # ✅ Enable streaming for better user experience
                max_tokens=1000,  # ✅ Allow longer responses
                temperature=0.6,  # ✅ Lower for more structured answers
                presence_penalty=0.5  # ✅ Encourages diverse and complete responses
            )

            async for chunk in response:
                if chunk.choices and chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content  # ✅ Stream response chunk by chunk

        # Stop timer and log response time
        response_time = time.time() - start_time
        logging.info(f"Chatbot response time: {response_time:.2f} seconds")

        return StreamingResponse(generate(), media_type="text/plain")

    except Exception as e:
        logging.error(f"Chatbot error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Chatbot error: {str(e)}")
