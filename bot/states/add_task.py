__all__ = ['dp']

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from ..config import dp
from aiogram.types import Message
from ..backend import controller
from datetime import datetime


class NewTask(StatesGroup):
    subject = State()
    description = State()
    deadline = State()
    confirm = State()


@dp.message_handler(commands=['add'], state=None)
async def add_task(message: Message):
    await message.answer('Введите тему задачи.')
    await NewTask.subject.set()


@dp.message_handler(state=NewTask.subject)
async def task_subject(message: Message, state: FSMContext):
    data = {
        'customer': message.from_user.id,
        'create_date': message.date,
        'subject': message.text
    }
    await state.update_data(data)
    await message.answer('Введите описание задачи:')
    await NewTask.next()


@dp.message_handler(state=NewTask.description)
async def task_description(message: Message, state: FSMContext):
    await state.update_data({'description': message.text})
    await message.answer('Введите дату выполнения')
    await NewTask.next()


@dp.message_handler(state=NewTask.deadline)
async def deadline(message: Message, state: FSMContext):
    raw_date = message.text
    raw_date = controller.str_to_date(raw_date)
    if raw_date is not None and raw_date >= datetime.now().date():
        await state.update_data({'deadline': raw_date})
        text = controller.preview_task(await state.get_data())
        await message.answer(f'Проверьте правильность задачи:\n{text}\n\nЕсли все хорошо - пришлите "ок" в ответ')
        await NewTask.next()
    else:
        await message.answer('Введите дату выполнения, больше или равную сегодняшней' \
                             'в формате "xxxx-xx-xx" или "xx-xx-xxxx"')


@dp.message_handler(state=NewTask.confirm)
async def confirm(message: Message, state: FSMContext):
    if message.text.lower() in ['ок', 'ok']:
        await message.reply('Все получилось')
        data = await state.get_data()
        controller.add_rec('task', **data)
        await state.reset_data()
        await state.finish()
    else:
        await message.reply('Введите "ок"')
