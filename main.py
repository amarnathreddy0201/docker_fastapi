from fastapi import FastAPI
import uvicorn
app = FastAPI()
from main1 import hello_amar


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/data")
def get_data():
    return {"data": "Hello World"}

@app.get("/final")
def final():
    return {"final": "Hello World"}

@app.get("/hello")
def hello():
    return {"hello": "Hello World"}

@app.get("hello2")
def hello2():
    return {"hello2": "Hello World"}

@app.get("love")
def love():
    return hello_amar()
