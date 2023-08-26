"""Module for FastAPI demo"""
from fastapi import FastAPI
app = FastAPI()


@app.get("/")
async def index():
    """
    Returns 'Hello World' message
    """
    return {"message": "Hello World"}
