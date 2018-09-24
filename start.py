import config
import telebot
import os
import download
import pdb
import logging
from telebot import types

bot = telebot.TeleBot(config.token)
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Hi there, I am CambridgeKyivBot. I can get mp3 from Youtube videos. Just send me video url and I will send you it's audio")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
	chat_id = message.chat.id
	url = message.text
	a =	download.get_video_info(url)
	if a == None:
		bot.reply_to(message, "Can't extract audio info")
	else:
		b = download.get_audio(url)
		file_id = open('{0}.mp3'.format(b), 'rb')
		bot.send_audio(chat_id, file_id, timeout=50)
		os.remove('{}.mp3'.format(b))
bot.polling()