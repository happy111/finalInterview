# File: app/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
from app.services.url_service import URLService

app = FastAPI(title="TinyURL Service")

service = URLService()

# Request body model
class URLRequest(BaseModel):
    long_url: HttpUrl

# Response model
class URLResponse(BaseModel):
    short_url: str

@app.post("/shorten", response_model=URLResponse)
def shorten_url(request: URLRequest):
    short_key = service.create_short_url(request.long_url)
    return URLResponse(short_url=f"http://short.url/{short_key}")

@app.get("/{short_key}")
def redirect_url(short_key: str):
    long_url = service.get_long_url(short_key)
    if not long_url:
        raise HTTPException(status_code=404, detail="URL not found or expired")
    return {"long_url": long_url}


#  http://127.0.0.1:8000 