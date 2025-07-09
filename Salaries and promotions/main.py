from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


@app.get('/hello/')
def hello(name:str):
    name = name.title().strip()
    return f'Hello {name}!'