from fastapi import FastAPI

app = FastAPI()

NAME = "NEXUS"

@app.get("/variables")
def get_variables():
    return {"NAME": NAME}
