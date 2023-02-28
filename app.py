from bot.config import get_parts
from bot.handlers import dp
from bot.states import dp
from bot.backend.controller import CONNECTION_STATUS
from aiogram import executor
from time import sleep


async def on_start(dpe):
    print('run, baby')
    owners = get_parts(['admins'])
    for owner in owners:
        await dpe.bot.send_message(owner, f'Бот... Запущен\n{CONNECTION_STATUS}')
        sleep(0.05)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_start)
