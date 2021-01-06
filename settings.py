from image import *

generators_list = """ Форматы картинок:
/image_preview - Аватарка(400x400)
/image_post - Пост-picture(800x600)
/image_long - Лонг-picture(800x200)
"""

image_generators = {
	'/image_preview': MakePreviewImage, 
	'/image_post': MakePostImage, 
	'/image_long': MakeLongImage
}

themes_list = """ Цветовые темы:
/theme_standart - Стандартный 
/theme_cloud - Розовое облако
/theme_green - Болото шрека"""

color_themes = {
	'/theme_standart': ('#ffffff', '#000000'),
	'/theme_cloud': ('#ffccdd', '#eeaaaa'),
	'/theme_green': ('#44aa66', '#ffffff')
}

token = '1513885476:AAFb37Uy1mcnkk_lQl09yGexKRMJvJBPXaw'

help_message = '''Рад вас видеть в боте PictureBot! 
Данный бот умеет создавать картинки с текстом. 
------
Как им пользоваться?
1) Вы сначала выбираете формат изображения и цвета
2) Вы отправляете боту текст, который нужно напечатать на изображении
-----
Команды:
/list_picture_formats - список команд для настройки формата изображения
/list_themes - Список команд для настройки цветов изображения
-----
Разработчик  
telegram: @googlewaitme
mail: kusok.apelbsina@gmail.com
'''
