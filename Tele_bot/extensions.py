import json
import requests
from config import keys


class ConvertionExeption(Exception):
    """Возникает в случае неудачной конвертации валюты"""

    pass


class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str) -> float:
        """Функция проверяет корректность введенных пользователем данных
        и возвращает количество сконвертированной валюты"""
        if quote == base:
            raise ConvertionExeption(f'Невозможно выполнить перевод одинаковых валют - {base}.')

        if quote not in keys.keys():
            raise ConvertionExeption(f'{quote} не является поддерживаемой валютой. Для того чтобы просмотреть список \
доступных валют используйте команду /values')

        if base not in keys.keys():
            raise ConvertionExeption(f'{base} не является поддерживаемой валютой. Для того чтобы просмотреть список \
доступных валют используйте команду /values')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f'Не удалось обработать количество - {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base * amount
