from settings import image_generators, color_themes 


class User:
	def __init__(self, image_generator='/image_post', color_theme='/theme_standart'):
		self.set_image_generator(image_generator)
		self.set_color_theme(color_theme) 

	def is_image_generator_exist(self, image_generator):
		return image_generator in image_generators

	def set_image_generator(self, image_generator):
		self.image_generator = image_generators[image_generator]

	def is_color_theme_exist(self, color_theme):
		return color_theme in color_themes

	def set_color_theme(self, color_theme):
		self.color_theme = color_themes[color_theme]
