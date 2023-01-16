from json import loads, dumps
from typing import List

from bank_app.user import User


def get_users() -> List[User]:
    """
    Получает список пользователей из бд
    :return: список из словарей, представляющих из себя пользователей
    """
    data = ""
    with open("users.json", "r") as db:
        data = "".join(db.readlines())
    users_data = loads(data)
    return [User(**element) for element in users_data]


def find_user_in_db(user: User) -> int:
    """
    Поиск порядкового номера пользователя в бд
    :return: индекс пользователеля
    """
    users = get_users()
    for element in enumerate(users):
        if user.id == element[1].id:
            return element[0]
    return -1


def create_original_list_from_users_list(users: List[User]) -> List[dict]:
    """
    Из списка объектов типа User создаёт список словарей, представляющих из себя объекты бд
    :param users: список объектов User
    :return: список объектов бд
    """
    result = []
    index = 0
    for user in users:
        result.append({})
        result[index]["id"] = user.id
        result[index]["pin"] = user.pin
        result[index]["balance"] = {
            key: value for key, value in zip(
                ("rub", "eur", "usd"),
                (user.balance.rub, user.balance.eur, user.balance.usd)
            )
        }
        result[index]["deposits"] = [{
            key: value for key, value in zip(("date", "type"), (deposit.date, deposit.type))
        } for deposit in user.deposits]
        index += 1
    return result


def update_user(user: User):
    """
    Обновляет данные пользователя в бд
    :param user: пользователь
    :return: None
    """
    users = get_users()
    index = find_user_in_db(user)
    users[index] = user
    data = create_original_list_from_users_list(users)
    with open("users.json", "w") as db:
        db.write(dumps(data))
