from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def check_new_image_format(message):
	if len(message.text) > 7 and message.text[:7] == '/image_':
		return True
	return False

def check_new_color_theme(message):
	if len(message.text) > 7 and message.text[:7] == '/theme_':
		return True
	return False 

def generate_image(text, user, filename):
	background_color, text_color = user.color_theme
	generator = user.image_generator(
		text=text,
		font_color=text_color,
		background_color=background_color,
		filename=filename
	)
	generator.generate_image()
