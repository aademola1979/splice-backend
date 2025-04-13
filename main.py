import os
from dotenv import load_dotenv
from fastapi import FastAPI, WebSocket, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
#from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
#from jose import jwt, JWTError
#from passlib.context import CryptContext
from starlette.exceptions import HTTPException as starletteHHTPException
from functools import lru_cache
from contextlib import asynccontextmanager
import config
from typing import Annotated
from database.database import init_db
from lib.next_auth.nextauth_jwt import NextAuthJWT

#ROUTES
from user.routers.user_routers import user_router
from address.routers.zone_router import zone_router
from address.routers.state_router import state_router
from user.routers.special_router import spec_router
from address.routers.lga_router import lga_router
from live_message.services import chat_endpoint

load_dotenv()

auth_secret = os.environ.get("NEXT_AUTH_SECRET")
JWT = NextAuthJWT(
    secret= auth_secret
)

@asynccontextmanager
async def lifespan(app:FastAPI):
    print(f'{app} starting up')
    await init_db()

    yield
    print(f'{app} shutting down')



app = FastAPI(
    title='Splice Seven',
    version='0.1.0',
    lifespan=lifespan,
)

#Routers
app.include_router( user_router)
app.include_router(zone_router)
app.include_router(state_router)
app.include_router(spec_router)
app.include_router(lga_router) 

client_url = os.environ.get("DEV_CLIENT_URL")
origins = [
    f"{client_url}",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.websocket("/ws/chat")
async def chat():
    return chat_endpoint(websocket=WebSocket)

@app.exception_handler(starletteHHTPException)
async def http_exception_handler(request, exc):
    print(f'{repr(exc)}')
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

@lru_cache()
def get_settings():
    return config.Settings()



@app.get("/")
async def greet(jwt:Annotated[dict, Depends(JWT)]):
    return {"Greet": f"Hi"}

