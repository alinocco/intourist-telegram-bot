import asyncio
import logging
import settings

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command


logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.TOKEN)

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


@dp.message(Command("bye"))
async def cmd_bye(message: types.Message):
    await message.answer("Bye!")


@dp.message()
async def cmd_start(message: types.Message):
    await message.answer(message.text.upper())


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
