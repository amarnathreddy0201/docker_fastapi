from typing import Union

from fastapi import FastAPI

import uvicorn
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/data")
def get_data():
    return {"data": "Hello World"}



@app.get("/datafinal")
def get_data():
    return {"data": "datafinal Hello World"}

uvicorn.run(app, host="0.0.0.0")
