from PIL import Image, ImageDraw, ImageFont
import os

class MakeImage:
    def __init__(self, text, background_color='white', font_color=(0, 0, 0), 
                    font_size=50, image_size=(400, 400), filename='photo.jpg'):
        self.text = text 
        self.background_color = background_color
        self.font_color = font_color
        self.font_size = font_size
        self.image_size = image_size
        self.filename = filename

    def generate_image(self):
        self.init_image()
        self.set_font()
        self.set_text_size()
        self.set_text_position()
        self.draw_image()
        # self.show_image()
        self.save_image()

    def init_image(self):
        self.image = Image.new('RGB', self.image_size, self.background_color)
        self.draw = ImageDraw.Draw(self.image)
        self.width, self.height = self.image_size

    def set_font(self):
        self.font = ImageFont.truetype(os.path.abspath('fonts/symbola.ttf'), self.font_size)

    def set_text_size(self):
        self.textwidth, self.textheight = self.draw.textsize(self.text, self.font)

    def set_text_position(self):
        x = (self.width - self.textwidth) // 2
        y = (self.height - self.textheight) // 2
        self.text_position = (x, y)

    def draw_image(self):
        self.draw.text(self.text_position, self.text, self.font_color, self.font)
       
    def show_image(self): 
        self.image.show()

    def save_image(self):
        self.image.save(self.filename)


class MakePreviewImage(MakeImage):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.image_size = (400, 400)
        self.font_size = 200

class MakePostImage(MakeImage):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.image_size = (800, 600)
        self.font_size = 70

class MakeLongImage(MakeImage):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.image_size = (800, 200)
        self.font_size = 70


if __name__ == '__main__':
    text = 'Zaripov Bulat'
    image = MakeLongImage(text=text).generate_image()
