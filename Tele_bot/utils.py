import json
import requests
from config import keys


class ConvertionExeption(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionExeption(f'Невозможно выполнить перевод одинаковых валют - {base}.')

        if quote not in keys.keys():
            raise ConvertionExeption(quote, 'не является поддерживаемой валютой. Для того чтобы просмотреть список \
доступных валют используйте комманду /values')

        if base not in keys.keys():
            raise ConvertionExeption(base, 'не является поддерживаемой валютой. Для того чтобы просмотреть список \
доступных валют используйте комманду /values')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f'Не удалось обработать количество - {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base
