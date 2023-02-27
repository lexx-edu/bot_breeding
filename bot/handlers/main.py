__all__ = ['dp']

from ..config import dp
from aiogram.types import Message
from ..backend import controller


help_txt = """Моя функция - таск-трекер:

/help - эта подсказка
/add - добавить задачу
"""


@dp.message_handler(commands=['start'])
async def start(message: Message):
    user_data = {
        'user_id': message.from_user.id,
        'user_name': message.from_user.first_name
    }
    controller.add_rec('user', **user_data)
    msg_text = f'Привет, {user_data["user_name"]}!\n\n' \
               f'Чтобы познакомится с функционалом, нажми /help'
    await message.answer(msg_text)


@dp.message_handler(commands=['help'])
async def help_hand(message: Message):
    await message.answer(help_txt)
