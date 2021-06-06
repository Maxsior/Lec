# Generated from .\LecParser.g4 by ANTLR 4.9.2
from typing import List, Union

from antlr4 import *

from LecParser import LecParser

import errors
import entities

from DrawEngine import DrawEngine
from Vector2 import Vector2
from VerticalCenterPacker import VerticalCenterPacker


# This class defines a complete listener for a parse tree produced by LecParser.
# noinspection PyPep8Naming
class LecParserListener(ParseTreeListener):
    variables = {}
    engine = DrawEngine()
    packer = VerticalCenterPacker(10, 10)
    parent_object = None
    is_var = None
    objects = []

    def _get_class(self, name: str):
        class_name = name.capitalize()
        if hasattr(entities, class_name):
            return getattr(entities, class_name)
        else:
            raise errors.UnknownObjectError(name)

    def _map_text(self, terminals) -> List[str]:
        return [term.symbol.text for term in terminals]

    def _map_value_terms(self, value_terms) -> List[Union[str, float, int]]:
        return [
            value.strip('"') if value.startswith('"') else
            float(value) if '.' in value else int(value)
            for value in self._map_text(value_terms)
        ]

    # Enter a parse tree produced by LecParser#root.
    def enterRoot(self, ctx: LecParser.RootContext):
        pass

    # Exit a parse tree produced by LecParser#root.
    def exitRoot(self, ctx: LecParser.RootContext):
        area = self.packer.pack(self.objects)

        area.expand(Vector2(2 * self.packer.padding))

        self.engine.set_size(int(area.width), int(area.height))

        # TODO use composite object
        for obj in self.objects:
            obj.translate(Vector2(self.packer.padding))
            obj.draw()

        self.engine.show()

    # Enter a parse tree produced by LecParser#variable.
    def enterVariable(self, ctx: LecParser.VariableContext):
        name = ctx.ID().symbol.text
        self.variables[name] = None

    # Exit a parse tree produced by LecParser#variable.
    def exitVariable(self, ctx: LecParser.VariableContext):
        name = ctx.ID().symbol.text
        self.variables[name] = None

    # Enter a parse tree produced by LecParser#obj.
    def enterObj(self, ctx: LecParser.ObjContext):
        if ctx.obj_call() is not None:
            return

        name = ctx.ID().symbol.text
        obj = self._get_class(name)(
            engine=self.engine,
            packer=self.packer,
            parent=self.parent_object,
        )

        if self.parent_object is not None:
            self.parent_object.add_child(obj)

        self.parent_object = obj

    # Exit a parse tree produced by LecParser#obj.
    def exitObj(self, ctx: LecParser.ObjContext):
        if self.parent_object.parent is None:
            self.objects.append(self.parent_object)

        self.parent_object.pack_children()
        self.parent_object = self.parent_object.parent

    # Enter a parse tree produced by LecParser#obj_call.
    def enterObj_call(self, ctx: LecParser.Obj_callContext):
        name = ctx.ID(0).symbol.text
        values = self._map_value_terms(ctx.VALUE())
        # vars = self._map_text(ctx.ID()[1:])

        obj = self._get_class(name)(
            engine=self.engine,
            packer=self.packer,
            parent=self.parent_object,
            values=values,
        )

        if self.parent_object is not None:
            self.parent_object.add_child(obj)

        self.parent_object = obj

    # Exit a parse tree produced by LecParser#obj_call.
    def exitObj_call(self, ctx: LecParser.Obj_callContext):
        pass


del LecParser
