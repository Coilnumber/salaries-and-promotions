from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from salaries_and_promotions.auth.jwt_auth import router as jwt_router
import uvicorn


app = FastAPI()
app.include_router(jwt_router)

@app.get('/')
def hello():
    return {'message': 'Hello, World!'}



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)