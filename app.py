import requests
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/joke")
def get_random_joke():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    responseJson = response.json()
    return responseJson["value"]



    