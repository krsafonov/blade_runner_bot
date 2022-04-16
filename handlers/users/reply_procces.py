import asyncio
import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from loader import dp

dp.message_handler()

latest_msg = {}

def create_keyboard(id, args):
    keyboard = InlineKeyboardMarkup(row_width=2)
    get_callback = CallbackData("get", "item_name")

    for i in range(len(args)):
        button = InlineKeyboardButton(text=args[i], callback_data=get_callback.new(item_name=f"{id}_{i}"))
        keyboard.insert(button)
    return keyboard


@dp.message_handler(Command("start"))  # made introduction and logic of collecting user's data
async def show_items(message: Message):
    msg = await message.answer(
        text="This Blade Runner Game by Kirill and Mikhail.", reply_markup=create_keyboard("start", ["Hello", "World"]))
    global latest_msg
    latest_msg[message.from_user.id] = msg


