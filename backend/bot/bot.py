import os
from aiogram import Bot, Dispatcher, types
from aiogram.webhook.aiohttp_server import SimpleRequestHandler
from aiohttp import web

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

async def on_startup(app: web.Application):
    await bot.set_webhook(
        url=os.getenv("WEBHOOK_URL") + "/webhook",
        drop_pending_updates=True
    )

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Добро пожаловать в CorpHelper!")

async def webhook_handler(request):
    url = str(request.url)
    if "/webhook" in url:
        update = types.Update(**await request.json())
        await dp.feed_update(bot=bot, update=update)
    return web.Response()

def setup_bot(app: web.Application):
    app.router.add_post("/webhook", webhook_handler)
    app.on_startup.append(on_startup)