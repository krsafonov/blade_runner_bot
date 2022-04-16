import asyncio
import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from loader import dp

from quest_driver import QuestDriver

dp.message_handler()

sessions = {}


def create_keyboard(id, labels, ways):
    keyboard = InlineKeyboardMarkup(row_width=2)

    for i in range(len(labels)):
        button = InlineKeyboardButton(text=labels[i], callback_data=f"{id}_{ways[i]}")
        keyboard.insert(button)
    return keyboard


@dp.message_handler(Command("start"))
async def show_items(message: Message):
    msg = await message.answer(
        text="This is Blade Runner Game by Kirill and Mikhail.", reply_markup=create_keyboard("start", ["Proceed"], ["Proceed"]))
    que = QuestDriver(file='Template.xlsx',
                      player={'Name': 'Peter', 'Age': 45, 'id': 1, 'rep_pol': 4})
    global sessions
    sessions[message.from_user.id] = que


@dp.callback_query_handler(text=["start_Proceed"])
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    global sessions
    que = sessions[call.from_user.id]
    a = que.update(1)
    await call.message.answer(a[0], reply_markup=create_keyboard("quest 1", a[2][1], a[2][2]))