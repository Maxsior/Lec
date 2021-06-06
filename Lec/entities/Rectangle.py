from Rectangle import Rectangle as Rect
from Vector2 import Vector2
from .BaseObject import BaseObject


class Rectangle(BaseObject):
    def get_self_bounds(self):
        size = Vector2(2 * self.packer.padding, self.packer.padding)
        return Rect(size=size)
