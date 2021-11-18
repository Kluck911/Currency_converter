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


bot.polling(none_stop=True)
