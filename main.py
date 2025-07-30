from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

BRANDS = {
    "NEXUS": {
        "NAME": "NEXUS",
        "DISCORD_URL": "https://discord.gg/nexus",
        "COLOR": "#00FFFF"
    },
    "ECORE": {
        "NAME": "ECORE",
        "DISCORD_URL": "https://discord.gg/ecore",
        "COLOR": "#FF00FF"
    }
}

@app.get("/variables/{brand}")
def get_variables(brand: str):
    brand = brand.upper()
    if brand in BRANDS:
        return BRANDS[brand]
    return JSONResponse(content={"error": "ERROR"}, status_code=404)
