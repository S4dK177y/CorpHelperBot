from fastapi import FastAPI
from bot.bot import setup_bot
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await setup_bot()

@app.get("/")
def read_root():
    return {"status": "ok"}