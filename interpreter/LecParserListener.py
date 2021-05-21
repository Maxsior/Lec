# Generated from .\LecParser.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LecParser import LecParser
else:
    from LecParser import LecParser

# This class defines a complete listener for a parse tree produced by LecParser.
class LecParserListener(ParseTreeListener):

    # Enter a parse tree produced by LecParser#root.
    def enterRoot(self, ctx:LecParser.RootContext):
        pass

    # Exit a parse tree produced by LecParser#root.
    def exitRoot(self, ctx:LecParser.RootContext):
        pass


    # Enter a parse tree produced by LecParser#variable.
    def enterVariable(self, ctx:LecParser.VariableContext):
        pass

    # Exit a parse tree produced by LecParser#variable.
    def exitVariable(self, ctx:LecParser.VariableContext):
        pass


    # Enter a parse tree produced by LecParser#obj.
    def enterObj(self, ctx:LecParser.ObjContext):
        pass

    # Exit a parse tree produced by LecParser#obj.
    def exitObj(self, ctx:LecParser.ObjContext):
        pass


    # Enter a parse tree produced by LecParser#obj_call.
    def enterObj_call(self, ctx:LecParser.Obj_callContext):
        pass

    # Exit a parse tree produced by LecParser#obj_call.
    def exitObj_call(self, ctx:LecParser.Obj_callContext):
        pass



del LecParser