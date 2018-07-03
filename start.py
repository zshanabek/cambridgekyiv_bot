import config
import telebot
import os
import download

bot = telebot.TeleBot(config.token)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
	chat_id = message.chat.id
	r = None
	url = message.text
	with ydl:
		r = ydl.extract_info(url, download=False) 
	audio = open('Rohirrim Charge (Battle of the Pelennor Fields) HD-l8yOdAqBFcQ.mp3', 'rb')
	bot.send_audio(chat_id, audio)
	os.remove('Rohirrim Charge (Battle of the Pelennor Fields) HD-l8yOdAqBFcQ.mp3')
bot.polling()