__all__ = ['dp']

from ..bot_init import dp
from aiogram.types import Message


@dp.message_handler()
async def ha_ha(message: Message):
    await message.answer(message.text)
