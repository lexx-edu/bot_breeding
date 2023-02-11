from aiogram import Bot, Dispatcher
import os


token = os.getenv('TOKEN')
bot = Bot(token)
dp = Dispatcher(bot)
