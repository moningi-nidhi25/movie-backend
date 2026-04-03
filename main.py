from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
from dotenv import load_dotenv


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (ok for now)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()

app = FastAPI()

API_KEY = os.getenv("OMDB_API_KEY")
BASE_URL = "http://www.omdbapi.com/"

@app.get("/")
def home():
    return {"message": "Movie Backend API is running 🚀"}

@app.get("/search")
def search_movies(query: str):
    params = {
        "apikey": API_KEY,
        "s": query
    }
    response = requests.get(BASE_URL, params=params).json()

    if response.get("Response") == "False":
        raise HTTPException(status_code=404, detail="Movie not found")

    return response

@app.get("/movie/{movie_id}")
def get_movie(movie_id: str):
    params = {
        "apikey": API_KEY,
        "i": movie_id
    }
    response = requests.get(BASE_URL, params=params).json()

    if response.get("Response") == "False":
        raise HTTPException(status_code=404, detail="Movie not found")

    return response
