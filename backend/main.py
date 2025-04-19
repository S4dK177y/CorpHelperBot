from fastapi import FastAPI
from bot.bot import setup_bot
from aiohttp import web
import uvicorn

app = FastAPI()
aioapp = web.Application()

setup_bot(aioapp)

@app.on_event("startup")
async def startup():
    await aioapp.startup()

@app.get("/")
def read_root():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))