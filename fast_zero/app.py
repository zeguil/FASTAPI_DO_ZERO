from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def reead_root():
    return {"msg": "Olar mundo 2"}
