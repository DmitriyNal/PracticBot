import aiogram
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import CommandStart

API_TOKEN = '8178599573:AAEXyUs1WG3Hz56ZtF8t6cVKTu48o9XIiZA'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет, бот готов к работе!")

@dp.message()
async def all_mesage(message: Message):
    await message.answer("Play command '\start'")





async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
