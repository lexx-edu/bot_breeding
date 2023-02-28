import yaml
from dotenv import dotenv_values
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


def set_config(config_path: str):
    with open(config_path, 'r') as file:
        result = yaml.safe_load(file)
        return result


def get_parts(part_path: list):
    result = config
    for part in part_path:
        result = result.get(part, None)
        if result is None:
            break
    return result


PATH_TO_CONFIG = dotenv_values('.env_02').get('config_file', 'config.yml')
STORAGE = MemoryStorage()

config = set_config(PATH_TO_CONFIG)
bot = Bot(get_parts(['init', 'token']))
dp = Dispatcher(bot, storage=STORAGE)
db_str = get_parts(['init', 'db_str'])
