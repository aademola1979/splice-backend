from fastapi import FastAPI, HTTPException, Response, Cookie
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from legalese.messages.routers import legalese_message_router


app = FastAPI()



origins = [
    "https://splice-seven.vercel.app",
    "http://localhost:3000",
    "http://localhost:5173"
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
    return {"Greet": "Demola won!"}