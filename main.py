import requests
from fastapi import FastAPI

API_URL = "https://afklol-api.onrender.com"

def get_api_data(params=None):
    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API connection error: {e}")
        return None

app = FastAPI()

@app.get("/")
async def root():
    data = get_api_data(params={"name": "NEXUS"})
    if data is None:
        return {"error": "Failed to fetch data from API"}
    return {"data": data}
