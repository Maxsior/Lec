from __future__ import annotations

from typing import Union


class Vector2:
    def __init__(self, x=0, y=None):
        self.x = x
        self.y = x if y is None else y

    @property
    def width(self):
        return self.x

    @property
    def height(self):
        return self.y

    def __add__(self, other: Union[Vector2, float, int]):
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        elif type(other) == int or type(other) == float:
            return Vector2(self.x + other, self.y + other)
        else:
            raise TypeError(f"unsupported operand type(s) for +: 'int' and '{type(other).__name__}'")

    def __sub__(self, other: Union[Vector2, float, int]):
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        elif type(other) == int or type(other) == float:
            return Vector2(self.x - other, self.y - other)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'Vector2({self.x}, {self.y})'

    def __iter__(self):
        yield self.x
        yield self.y
