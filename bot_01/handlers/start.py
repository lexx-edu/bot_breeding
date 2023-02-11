__all__ = ['dp']

from ..bot_init import dp
from aiogram.types import Message, ReplyKeyboardRemove
from ..keyboards import kb_startmenu


@dp.message_handler(commands=['start'])
async def start(message: Message):
    answer = f'Привет тебе, {message.from_user.first_name}!' \
             f' Это {message.message_id} фраза.'
    await message.answer(text=answer, reply_markup=kb_startmenu)
# await message.answer(text=answer, reply_markup=ReplyKeyboardRemove())  # Грохаем клаву
