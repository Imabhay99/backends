
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from inference import run_tryon_from_urls  # This should be implemented correctly
import sys
import os

# Add the path to 'dressing-in-order-main' so that imports work
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'dressing-in-order-main')))

# Initialize FastAPI app
app = FastAPI()

# CORS Middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace this with your frontend URL for better security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model to define request body
class TryOnRequest(BaseModel):
    person_url: str
    cloth_url: str

# Health check route (optional but recommended)
@app.get("/")
def root():
    return {"status": "Dressing In Order API is running!"}

# Serve favicon.ico
@app.get("/favicon.ico")
async def favicon():
    return FileResponse("static/favicon.ico")

