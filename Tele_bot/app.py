import telebot
from config import keys, TOKEN
from extensions import CryptoConverter, ConvertionExeption

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help_(message: telebot.types.Message) -> None:
    """Вызов сообщения с описанием работы бота"""

    text = 'Введите тип конвертируемой валюты в следующем виде:\n<имя валюты> <в какую валюту ' \
           'перевести> <количество переводимой валюты>.\nВсе значения вводите через пробел.\n' \
           'Для того чтобы просмотреть список доступных валют, используйте комманду /values '
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message) -> None:
    '''Функция показывает сообщение со списком доступных валют'''

    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def get_price(message: telebot.types.Message) -> None:
    '''Функция получает запрос пользователя, и возвращает сообщение,
     которое содержит введенные валюты и значение после конвертации'''
    try:
        values_ = message.text.split(' ')

        if len(values_) != 3:
            raise ConvertionExeption('Неверное количество параметров')

        quote, base, amount = values_
        total_base = CryptoConverter.get_price(quote, base, amount)
    except ConvertionExeption as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
