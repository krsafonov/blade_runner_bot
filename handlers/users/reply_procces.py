import asyncio
import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from loader import dp


dp.message_handler()


@dp.message_handler(Command("start"))  # made introduction and logic of collecting user's data
async def show_items(message: Message):
    await message.answer(
        text="This Blade Runner Game by Kirill and Mikhail.")
