__all__ = ['dp']

from ..bot_init import dp
from aiogram.types import Message


@dp.message_handler(commands=['help'])
async def help(message: Message):
    await message.answer(text='Че те надо?')
