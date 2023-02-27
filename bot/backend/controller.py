from . import engine

CONNECTION_STATUS = engine.check_connect()


def add_rec(type_rec, **kwargs):
    if type_rec == 'user':
        engine.user_add(**kwargs)
