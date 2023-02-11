from bot_01.handlers import dp
from aiogram import executor
import os


async def on_start(dpe):
    owner = os.getenv('owner')
    await dpe.bot.send_message(owner, 'Бот запущен')
    print('run, baby')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_start)
