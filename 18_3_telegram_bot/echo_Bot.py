import telebot

TOKEN = '2133939877:AAHWM6SXH6w9VYW6eC3JIPDaSkAWG3jEmbY'
bot = telebot.TeleBot(TOKEN)


# @bot.message_handler(commands=['start', 'help'])
# def handle_start_help(message):
#    bot.reply_to(message, 'This is a message handler')

# ---------------------------------------------------------

# @bot.message_handler(content_types=['document', 'audio'])
# def handle_docs_audio(message):
#    pass


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: telebot.types.Message):
    bot.send_message(message.chat.id, f"Welcome, \n{message.chat.username}")


@bot.message_handler(content_types=['voice', ])
def repeat(message: telebot.types.Message):
    bot.send_message(message.chat.id, "У тебя очень красивый голос")


@bot.message_handler(content_types=['photo', ])
def photo_mem(message):
    bot.reply_to(message, f'Nice meme XDD\n{message.chat.username}')


bot.polling(none_stop=True)
