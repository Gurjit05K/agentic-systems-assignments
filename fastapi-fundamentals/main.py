from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# Create FastAPI app
app = FastAPI(
    title="Query Parameters Demo",
    description="Simple GET endpoint with optional name and age",
    version="1.0"
)


class SearchResponse(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None


# GET endpoint /search with optional query parameters
@app.get("/search", response_model=SearchResponse)
async def search(
    name: Optional[str] = None,  
    age: Optional[int] = None     
):
    """
    Returns the received query parameters as JSON.
    Both name and age are optional.
    """
    return {
        "name": name,
        "age": age
    }