from __future__ import annotations

from typing import List, Union
from operator import attrgetter

from Rectangle import Rectangle
from Vector2 import Vector2
from entities import BaseObject

Number = Union[int, float]


class VerticalCenterPacker:
    def __init__(self, margin: Number = 0, padding: Number = 0):
        self.margin = margin
        self.padding = padding

    def pack(self, objects: List[BaseObject]):
        if not objects:
            return

        max_width = max(map(attrgetter('bounds.width'), objects))
        area = Rectangle(start=(0, 0), size=(max_width, 0))

        for obj in objects:
            h_offset = (area.width - obj.bounds.width) / 2
            new_position = area.bottom_left + Vector2(h_offset, 0)
            obj.move_to(new_position)
            area += obj.bounds
            area.expand(Vector2(0, self.margin))

        area.expand(Vector2(0, -self.margin))

        return area

    def make_padding(self, obj: BaseObject):
        for child in obj.children:
            child.translate(Vector2(self.padding))
        obj.bounds.expand(Vector2(2 * self.padding))
