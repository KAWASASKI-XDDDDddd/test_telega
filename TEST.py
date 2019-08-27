import telebot

bot = telebot.TeleBot("870213358:AAFaYU3mmtMNnoIrvULDibxSIRmUAHYOlm8")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	bot.reply_to(message, message.text)

bot.polling( none_stop = True )