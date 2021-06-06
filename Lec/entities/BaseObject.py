from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Optional, Union

from Vector2 import Vector2
from Rectangle import Rectangle

Value = Union[float, int, str]


class BaseObject(ABC):
    _bounds = None

    def __init__(self, engine, packer, parent: Optional[BaseObject] = None, values: List[Value] = []):
        self.engine = engine
        self.packer = packer
        self.parent = parent
        self.values = values
        self.children: List[BaseObject] = []

    @property
    def bounds(self):
        if self._bounds is None:
            self._calc_bounds()

        return self._bounds

    def add_child(self, obj):
        self.children.append(obj)

    def set_values(self, values):
        self.values = values

    def pack_children(self):
        self.packer.pack(self.children)

    def draw(self):
        self.engine.draw(self)
        for child in self.children:
            child.draw()

    def move_to(self, position: Vector2):
        self.translate(position - self.bounds.top_left)

    def translate(self, direction: Vector2):
        self.bounds.translate(direction)
        for child in self.children:
            child.translate(direction)

    def _calc_bounds(self):
        if not self.children:
            self._bounds = self.get_self_bounds()
            return

        self._bounds = Rectangle(x0=0, x1=0, y0=0, y1=0)

        for child in self.children:
            self._bounds += child.bounds
        self.packer.make_padding(self)

    @abstractmethod
    def get_self_bounds(self):
        pass

    # @property
    # @abstractmethod
    # def value_validator(self) -> BaseValidator:
    #     pass ValueInheritanceValidator([Text, Color])
    #
    # @property
    # @abstractmethod
    # def child_validator(self) -> BaseValidator:
    #     pass
