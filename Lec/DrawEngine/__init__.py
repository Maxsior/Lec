from PIL import Image, ImageDraw, ImageFont
import os.path

from entities import *
from entities.BaseObject import BaseObject


class DrawEngine:
    # _im = Image.open('DrawEngine/error.jpeg')
    _im = None
    canvas = None

    font_path = os.path.join(os.path.dirname(__file__), './Roboto-Regular.ttf')

    font = ImageFont.truetype(font_path, 40)

    colors = {
        "secondary": (255, 255, 255, 0),
        "primary": (0, 0, 0, 255),
    }

    def set_size(self, w: int, h: int):
        self._im = Image.new("RGBA", (w, h), (255, 255, 255, 255))
        self.canvas = ImageDraw.Draw(self._im)

    def draw(self, obj: BaseObject):
        assert self.canvas is not None

        if isinstance(obj, Text):
            self.canvas.text(tuple(obj.bounds.top_left), obj.values[0], fill=self.colors["primary"], font=self.font)
        elif isinstance(obj, Rectangle):
            self.canvas.rectangle([tuple(obj.bounds.top_left), tuple(obj.bounds.bottom_right)], outline=self.colors["primary"])
        else:
            print('Unknown object')

    def get_text_size(self, text):
        return self.font.getsize(text)

    def show(self):
        self._im.show()

    def save(self, fname):
        self._im.save(fname, "PNG")
