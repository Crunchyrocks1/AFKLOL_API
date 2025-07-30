import requests
from fastapi import FastAPI

app = FastAPI()

# Your stored variables
NAME = "NEXUS"

API_URL = "https://afklol-api.onrender.com"

def get_api_data(name):
    try:
        response = requests.get(API_URL, params={"name": name})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API connection error: {e}")
        return None

@app.get("/")
def root():
    data = get_api_data(NAME)
    if data:
        return {"api_response": data}
    else:
        return {"error": "No data received from API"}
