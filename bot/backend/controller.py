from . import engine
from . import formater

CONNECTION_STATUS = engine.check_connect()


def add_rec(type_rec, **kwargs):
    if type_rec == 'user':
        engine.user_add(**kwargs)
    elif type_rec == 'task':
        engine.task_add(**kwargs)


def preview_task(data):
    if isinstance(data, dict):
        user_name = engine.get_user(data['customer'])
        if user_name is not None:
            data['customer'] = user_name[1]
        return formater.preview_dict(data)


def str_to_date(str_date: str):
    return formater.parse_date(str_date)
