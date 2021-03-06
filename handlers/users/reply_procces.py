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

uni_numbers = [
    "1️⃣",
    "2️⃣",
    "3️⃣",
    "4️⃣",
    "5️⃣",
    "6️⃣",
    "7️⃣",
    "8️⃣",
    "9️⃣",
]


def create_keyboard(id, ways):
    keyboard = InlineKeyboardMarkup(row_width=2)

    for i in range(len(ways)):
        button = InlineKeyboardButton(text=uni_numbers[i], callback_data=f"{id}_{ways[i]}")
        keyboard.insert(button)
    return keyboard


@dp.message_handler(Command(["start", "restart"]))
async def show_items(message: Message):
    que = QuestDriver(file='Template.xlsx',
                      player={'Name': message.from_user.first_name,
                              'Age': 45, 'id': 1,
                              'rep_pol': 4,
                              'humanity': 0})
    global sessions
    sessions[message.from_user.id] = que
    a = que.show()
    msg = a[0].replace('\\n', '\n').replace('\\t', '\t') + "\n\n Your options:\n" + "\n".join([uni_numbers[i] + "\t" + j for i, j in enumerate(a[2][1])])
    await message.answer(msg, reply_markup=create_keyboard("quest", a[2][2]))


@dp.callback_query_handler(text_contains="quest")
async def sub(call: CallbackQuery):
    await call.answer()
    global sessions
    que = sessions[call.from_user.id]
    try:
        way = int(float(call.data[6:]))
    except ValueError:
        way = call.data[6:]
    try:
        a = que.update(way)
        msg = a[0].replace('\\n', '\n').replace('\\t', '\t') + "\n\n Your options:\n" + "\n".join([uni_numbers[i] + "\t" + j for i, j in enumerate(a[2][1])])
        await call.message.answer(msg, reply_markup=create_keyboard("quest", a[2][2]))
        sessions[call.from_user.id] = que
    except ValueError:
        await call.message.answer("Please, don't press the buttons of the previous messages. If you want to change "
                                  "your decision you can type /restart command (the game will start from the "
                                  "beginning).")
