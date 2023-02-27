import sqlalchemy
from . import base_init as bi


def req_exequte(req: str):
    req = sqlalchemy.text(req)
    with bi.engine.connect() as connect:
        result = connect.execute(req)
        connect.commit()
    if result is not None:
        return result


def check_connect():
    if bi.engine is None:
        return 'База данных... Fail'
    for req in bi.check_base_req:
        req_exequte(req)
    return 'База данных... OK'


def user_add(user_id, user_name):
    user_exist = check_user(user_id)
    if not user_exist:
        req = f"""
            insert into bot_users values ({user_id}, '{user_name}', 0);
        """
        req_exequte(req)
    pass


def check_user(user_id):
    req = f"""
    select id from bot_users where id = {user_id}
    """
    cursor = req_exequte(req)
    if cursor.one_or_none() is None:
        return False
    else:
        return True
