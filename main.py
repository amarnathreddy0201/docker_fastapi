from fastapi import FastAPI
import uvicorn
app = FastAPI()


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