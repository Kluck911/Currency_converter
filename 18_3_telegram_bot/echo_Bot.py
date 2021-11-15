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
def send_welcome(message):
    bot.send_message(message.chat.id, f"Welcome, \ c{message.chat.username}")


bot.polling(none_stop=True)
