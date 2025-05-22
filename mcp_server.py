from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Dict, List, Any, Optional
import uvicorn

# Define the request and response models based on MCP specification
class MCPRequest(BaseModel):
    inputs: str
    parameters: Dict[str, Any] = {}

class ResponseChoice(BaseModel):
    index: int
    message: Dict[str, str]

class MCPResponse(BaseModel):
    choices: List[ResponseChoice]

# Create the FastAPI app
app = FastAPI(title="Simple MCP Server")

@app.post("/v1/generate", response_model=MCPResponse)
async def generate(request: MCPRequest):
    # Log the incoming request
    print(f"Received request: {request.inputs}")
    
    # Create a simple response
    response_text = "Hello, World! This is my MCP server."
    
    # Return the response with a single choice
    return MCPResponse(
        choices=[
            ResponseChoice(
                index=0,
                message={"content": response_text}
            )
        ]
    )

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    # Start the server
    # Cloud Run will set the PORT environment variable
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("mcp_server:app", host="0.0.0.0", port=port)
