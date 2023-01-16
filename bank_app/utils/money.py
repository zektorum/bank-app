from bank_app.user import User
from bank_app.utils.users import update_user


def replenish_balance(user: User, currency: str, amount: float) -> int:
    if currency == "RUB":
        user.balance.rub += amount
    if currency == "USD":
        user.balance.usd += amount
    if currency == "EUR":
        user.balance.eur += amount
    update_user(user)
    return 1


def remove_money(user: User, currency: str,  amount: float) -> int:
    if currency == "RUB" and user.balance.rub - amount >= 0:
        user.balance.rub -= amount
    elif currency == "USD" and user.balance.usd - amount >= 0:
        user.balance.usd -= amount
    elif currency == "EUR" and user.balance.eur - amount >= 0:
        user.balance.eur -= amount
    else:
        return -1
    update_user(user)
    return 1
