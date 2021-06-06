from Rectangle import Rectangle as Rect
from .BaseObject import BaseObject


class Text(BaseObject):
    def get_self_bounds(self):
        size = self.engine.get_text_size(self.values[0])
        return Rect(size=size)
