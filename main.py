from fastapi import FastAPI, HTTPException, Response, Cookie
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()



origins = [
    "https://splice-seven.vercel.app",
    "http://localhost:3000"
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def greet():
    return {"Greet": "Demola won! New"}

@app.get("/profile")
async def go_app():
    return {"profile":{
        "first_name":"Ademola",
        "middle_name":"Oriyomi",
        "last_name":"Adeniji",
        "bio_data":{
            "age":34,
            "height":4.5,
            "weight": 45
        }

    }}