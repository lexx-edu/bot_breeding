__all__ = ['kb_startmenu']

from aiogram.types import ReplyKeyboardMarkup  # доска
from aiogram.types import KeyboardButton  # клавиша
from aiogram.types import ReplyKeyboardRemove  # Удаляет клавиатуру после нажатия


kb_startmenu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# resize_keyboard - позволяет подогнать размер доски под что-то адекватное
# one_time_keyboard - скрывает клавиатуру поле выбора


btn_help = KeyboardButton('/help')
btn_test = KeyboardButton('/test', request_location=True)

# kb_startmenu.add(btn_help, btn_test)  # В одну строку
kb_startmenu.add(btn_help).add(btn_test)  # Каждый .add порождает строку
