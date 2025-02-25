from fastapi import FastAPI, HTTPException, Response, Cookie, Depends
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as starletteHHTPException
from contextlib import asynccontextmanager
from dotenv import load_dotenv
import os
from typing import Union
from functools import lru_cache
import config
from todo_app.routers import todo as todo_router



load_dotenv()
secret = os.environ['DATABASE_NAME']
@asynccontextmanager
async def lifespan(app: FastAPI):
    print('Server is starting')
    yield
    print('Server is shutting down')



app = FastAPI(
    title= 'Splice7 backend',
    version= '0.1.0',
    description= 'Backend service for splice7',
    lifespan=lifespan
)

app.include_router(todo_router.router)



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

@app.exception_handler(starletteHHTPException)
async def http_exception_handler(request, exc):
    print(f'{repr(exc)}')
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

@lru_cache()
def get_settings():
    return config.Settings()



@app.get('/con')
def read_setting(setting: config.Settings = Depends(get_settings)):
    print(setting.app_name)
    return "Still learning"

@app.get("/")
async def greet():
    return {"Greet": f"{secret}"}

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

@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}