from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

import asyncio
import logging
import sys

from setings.token_function import get_token
from function.bot_function import aprove_tg_id

b_token = get_token("BOT")
g_token = get_token("GPT")

BOT = Bot(token=b_token)

dp = Dispatcher()


@dp.message(CommandStart())
async def comand_start(message: Message):
    if aprove_tg_id(id=message.from_user.id):
        await message.answer(f"Welcome back, {message.from_user.full_name}!")
    else:
        await message.answer("Hi! Im crypto bot!\nRegister now!")


@dp.message(Command("help"))
async def comand_help(message: Message):
    await message.answer("Write your question")


async def main():
    await dp.start_polling(BOT)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
