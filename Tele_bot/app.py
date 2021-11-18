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


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Введите тип конвертируемой валюты в следующем виде:\n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты>\n Для того чтобы просмотреть список доступных валют \
ввкдите комманду </values>'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    quote, base, amount = message.text.split(' ')
    r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
    text = json.loads(r.content)
    bot.send_message(message.chat.id, "{0}: {1}".format(base, text.get(keys[base])))


bot.polling(none_stop=True)
