from fastapi import FastAPI, HTTPException

app = FastAPI()

brands = {
    "NEXUS": {
        "NAME": "NEXUS",
        "DISCORD_URL": "https://discord.gg/Aq8uTZqVZN",
        "COLOR": "blue"
    },
    "ECORE": {
        "NAME": "ECORE",
        "DISCORD_URL": "https://discord.gg/ecore",
        "COLOR": "green"
    },
}

@app.get("/variables/{brand_name}")
def get_variables(brand_name: str):
    brand_data = brands.get(brand_name.upper())
    if not brand_data:
        raise HTTPException(status_code=404, detail="Brand not found")
    return brand_data
