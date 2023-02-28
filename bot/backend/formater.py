import datetime


def preview_dict(task):
    text = str(f"""

Владелец: {task['customer']}
Дата создания: {str(task['create_date'])[:10]}
Срок выполнения: {task['deadline']}

Тема: {task['subject']}

Описание:
{task['description']}
   
    """)
    return text


def parse_date(str_date: str):
    sep = ['.', '-', '/']
    for i in sep:
        if i in str_date:
            res = str_date.split(i)
            if len(res[0]) != 4:
                res = res[::-1]
            res = datetime.date(int(res[0]), int(res[1]), int(res[2]))
            return res
    return None
