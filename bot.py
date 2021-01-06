import telebot
import settings
import helpers
from models import User

bot = telebot.TeleBot(settings.token, parse_mode=None)
users = dict()


@bot.message_handler(commands=['start', 'help'])
def send_help(message):
	if not message.chat.id in users:
		users[message.chat.id] = User()
	bot.reply_to(message, settings.help_message)


@bot.message_handler(commands=['list_themes'])
def send_themes_list(message):
	bot.reply_to(message, settings.themes_list)

@bot.message_handler(commands=['list_picture_formats'])
def send_generators_list(message):
	bot.reply_to(message, settings.generators_list)


@bot.message_handler(func=helpers.check_new_image_format)
def set_new_image_format(message):
	if not message.chat.id in users:
		users[message.chat.id] = User()
	users[message.chat.id].set_image_generator(message.text)
	bot.reply_to(message, 'Новый формат изображения установлен!')

@bot.message_handler(func=helpers.check_new_color_theme)
def set_color_theme(message):
	if not message.chat.id in users:
		users[message.chat.id] = User()
	users[message.chat.id].set_color_theme(message.text)
	bot.reply_to(message, 'Новая тема установлена!')


@bot.message_handler(func=lambda message: True)
def send_image(message):
	print(message.chat.id)
	if not message.chat.id in users:
		bot.reply_to(message, settings.help_message)
	else:
		helpers.generate_image(text=message.text, user=users[message.chat.id], filename='photo.jpg')
		photo = open('photo.jpg', 'rb')
		bot.send_photo(message.chat.id, photo)


bot.polling()
