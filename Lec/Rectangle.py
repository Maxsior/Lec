from __future__ import annotations

from typing import Union

from Vector2 import Vector2


class Rectangle:
    def __init__(self, **kwargs):
        if "x0" in kwargs and "x1" in kwargs and "y0" in kwargs and "y1" in kwargs:
            x0 = kwargs["x0"]
            y0 = kwargs["y0"]
            x1 = kwargs["x1"]
            y1 = kwargs["y1"]
        elif "size" in kwargs:
            x0, y0 = kwargs.get("start", (0, 0))
            x1, y1 = kwargs["size"]
            x1 += x0
            y1 += y0
        else:
            raise ValueError("Can't parse area init params")

        self._x0 = min(x0, x1)
        self._y0 = min(y0, y1)
        self._x1 = max(x0, x1)
        self._y1 = max(y0, y1)

    @property
    def top_left(self):
        return Vector2(self._x0, self._y0)

    @property
    def top_right(self):
        return Vector2(self._x1, self._y0)

    @property
    def bottom_right(self):
        return Vector2(self._x1, self._y1)

    @property
    def bottom_left(self):
        return Vector2(self._x0, self._y1)

    @property
    def width(self):
        return self._x1 - self._x0

    @property
    def height(self):
        return self._y1 - self._y0

    @property
    def size(self):
        return Vector2(self.width, self.height)

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

    def align(self):
        self._x1 = self.width
        self._y1 = self.height
        self._x0 = self._y0 = 0

    def translate(self, direction: Vector2):
        self._x0 += direction.x
        self._x1 += direction.x
        self._y0 += direction.y
        self._y1 += direction.y

    def is_square(self):
        return self.width == self.height

    def expand(self, amount):
        if isinstance(amount, Vector2):
            self._x1 += amount.x
            self._y1 += amount.y
        elif type(amount) == int or type(amount) == float:
            self._x1 += amount
            self._y1 += amount
        else:
            raise TypeError(f"unsupported operand type(s) for 'expand': 'int' and '{type(amount).__name__}'")

    # unite rectangles
    def __add__(self, other: Union[Rectangle, float, int]):
        if isinstance(other, Rectangle):
            return Rectangle(
                x0=min(self._x0, other._x0),
                y0=min(self._y0, other._y0),
                x1=max(self._x1, other._x1),
                y1=max(self._y1, other._y1),
            )
        else:
            raise TypeError(f"unsupported operand type(s) for +: 'int' and '{type(other).__name__}'")

    def __repr__(self):
        return f'Rectangle({self.top_left}, {self.bottom_right}))'
