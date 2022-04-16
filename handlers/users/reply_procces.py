import asyncio
import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from loader import dp

from quest_driver import QuestDriver

dp.message_handler()


def create_keyboard(id, args):
    keyboard = InlineKeyboardMarkup(row_width=2)

    for i in range(len(args)):
        button = InlineKeyboardButton(text=args[i], callback_data=f"{id}_{args[i]}")
        keyboard.insert(button)
    return keyboard


@dp.message_handler(Command("start"))
async def show_items(message: Message):
    msg = await message.answer(
        text="This is Blade Runner Game by Kirill and Mikhail.", reply_markup=create_keyboard("start", ["Proceed"]))
    que = QuestDriver(file='Template.xlsx',
                      player={'Name': 'Peter', 'Age': 45, 'id': message.from_user.id, 'rep_pol': 4})


@dp.callback_query_handler(text=["start_Proceed"])
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    msg = await call.message.answer("Well Done!")
