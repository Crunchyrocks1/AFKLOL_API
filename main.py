from fastapi import FastAPI, HTTPException

app = FastAPI()

brands = {
    "NEXUS": {
        "NAME": "NEXUS",
        "DISCORD_URL": "",
        "COLOR": "blue"
    },
    "ECORE": {
        "NAME": "ECORE",
        "DISCORD_URL": "https://discord.gg/your-ecore-link",
        "COLOR": "green"
    },
    # Add more brands here
}

@app.get("/variables")
def no_default_brand():
    # No default brand allowed, so always raise error if no brand specified
    raise HTTPException(status_code=400, detail="Brand not specified. Use /variables/{brand_name}")

@app.get("/variables/{brand_name}")
def get_variables(brand_name: str):
    brand_data = brands.get(brand_name.upper())
    if not brand_data:
        raise HTTPException(status_code=404, detail="Brand not found")
    return brand_data
