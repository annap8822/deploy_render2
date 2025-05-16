from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def homepage():
    return "Ciao, questa è l'homepage"