from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as starletteHHTPException
from functools import lru_cache
from contextlib import asynccontextmanager
import config
from databse.database import init_db
from user.routers.routers import user_router
from address.routers.zone_router import zone_router
from address.routers.state_router import state_router



@asynccontextmanager
async def lifespan(app:FastAPI):
    print('App starting up')
    await init_db()

    yield
    print('App shutting down')



app = FastAPI(
    title='Splice Seven',
    version='0.1.0',
    lifespan=lifespan,
)

#Routers
app.include_router( user_router)
app.include_router(zone_router)
app.include_router(state_router)




origins = [
    "https://splice-seven.vercel.app",
    "http://localhost:3000",
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



@app.get("/")
async def greet():
    return {"Greet": f"Hi"}

