from aiogram import Bot, Dispatcher, types
import os

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

async def setup_bot():
    await bot.delete_webhook()
    await bot.set_webhook(f"{os.getenv('WEBHOOK_URL')}/webhook")
    
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Добро пожаловать в CorpHelper!")