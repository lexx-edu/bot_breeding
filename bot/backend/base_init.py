import sqlalchemy
from ..config import db_str


try:
    engine = sqlalchemy.create_engine(db_str)
except 'ArgumentError':
    engine = None

check_base_req = [
        """
        CREATE TABLE IF NOT EXISTS bot_users (
            id INTEGER,
            name TEXT,
            is_block INTEGER,
            CONSTRAINT users_PK PRIMARY KEY (id)
        );""",

        """
        CREATE TABLE IF NOT EXISTS bot_tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer INTEGER,
            create_date TEXT, 
            subject TEXT,
            description TEXT,
            deadline TEXT, 
            status INTEGER,
            attach TEXT,
            is_close INTEGER,  
            is_available INTEGER   
        );""",

        """
        CREATE TABLE IF NOT EXISTS bot_statuses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT,
            is_block INTEGER
        );""",

        """
        CREATE TABLE IF NOT EXISTS bot_work_log (
            user_id INTEGER,
            task_id TEXT,
            start_date TEXT,
            finish_date TEXT,
            CONSTRAINT work_log_PK PRIMARY KEY (user_id,task_id)
        )
        """
        ]