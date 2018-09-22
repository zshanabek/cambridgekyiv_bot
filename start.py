import config
import telebot
import os
import download
import pdb
import logging
from telebot import types

bot = telebot.TeleBot(config.token)
logger = telebot.logger
# telebot.logger.setLevel(logging.DEBUG)
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Hi there, I am YoutubeBot.")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
	chat_id = message.chat.id
	url = message.text
	a =	download.get_video_info(url)
	if a == None:
		bot.reply_to(message, "Can't extract audio info")
	else:
		keyboard = types.InlineKeyboardMarkup()
		yes = types.InlineKeyboardButton(text="Download", callback_data = 'yes ' + url)
		no = types.InlineKeyboardButton(text="Cancel", callback_data = 'no ')
		keyboard.add(yes, no)
		bot.send_message(chat_id, a, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	chat_id = call.message.chat.id
	if call.message:
		a = call.data.split()
		if a[0] == 'yes':
			a = download.get_audio(a[1])
			audio = open('{0}.mp3'.format(a), 'rb')
			bot.send_audio(chat_id, audio)
			os.remove('{}.mp3'.format(a))
		else:
			pass
bot.polling()