import requests
import telebot
import json


TOKEN = '2102115834:AAEzx3WrkrC1U6K2COhmUEgZmtm-Pn2XICQ'


bot = telebot.TeleBot(TOKEN)

keys = {
    'биткоин': 'BTC',
    'эфириум': 'ETH',
    'доллар': 'USD',
}


class ConvertionExeption(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionExeption(f'Невозможно выполнить перевод одинаковых валют - {base}.')

        if quote not in keys.keys():
            raise ConvertionExeption(quote, 'не является поддерживаемой валютой. Для того чтобы просмотреть список \
        доступных валют введите комманду </values>')

        if base not in keys.keys():
            raise ConvertionExeption(base, 'не является поддерживаемой валютой. Для того чтобы просмотреть список \
        доступных валют введите комманду </values>')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f'Не удалось обработать количество - {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Введите тип конвертируемой валюты в следующем виде:\n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты>\n Для того чтобы просмотреть список доступных валют \
введите комманду </values>'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    values_ = message.text.split(' ')

    if len(values_) != 3:
        raise ConvertionExeption('Неверное количество параметров')

    quote, base, amount = values_
    total_base = CryptoConverter.convert(quote, base, amount)


    text = f'Цена {amount} {quote} в {base} - {float(total_base) * float(amount)}'
    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
