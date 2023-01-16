from bank_app import exchange_rates
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


def convert_currency(currency_from: str, currency_to: str, amount: float) -> float:
    if currency_from == "RUB" and currency_to == "EUR":
        return amount * exchange_rates.RUB_TO_EUR
    elif currency_from == "RUB" and currency_to == "USD":
        return amount * exchange_rates.RUB_TO_USD
    elif currency_from == "USD" and currency_to == "RUB":
        return amount * exchange_rates.USD_TO_RUB
    elif currency_from == "USD" and currency_to == "EUR":
        return amount * exchange_rates.USD_TO_EUR
    elif currency_from == "EUR" and currency_to == "RUB":
        return amount * exchange_rates.EUR_TO_RUB
    elif currency_from == "EUR" and currency_to == "USD":
        return amount * exchange_rates.EUR_TO_USD
