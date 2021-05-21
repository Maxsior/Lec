# Generated from .\LecLexer.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


if __name__ is not None and "." in __name__:
    from .LecLexerBase import LecLexerBase
else:
    from LecLexerBase import LecLexerBase


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("\\\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\3")
        buf.write("\3\3\5\3\36\n\3\3\4\3\4\3\4\7\4#\n\4\f\4\16\4&\13\4\3")
        buf.write("\5\3\5\3\6\6\6+\n\6\r\6\16\6,\3\6\3\6\6\6\61\n\6\r\6\16")
        buf.write("\6\62\5\6\65\n\6\3\7\3\7\3\b\3\b\6\b;\n\b\r\b\16\b<\3")
        buf.write("\b\3\b\3\t\3\t\7\tC\n\t\f\t\16\tF\13\t\3\t\3\t\3\n\6\n")
        buf.write("K\n\n\r\n\16\nL\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\f\5\fY\n\f\3\f\3\f\3<\2\r\3\6\5\7\7\b\t\2\13\t\r")
        buf.write("\2\17\n\21\13\23\f\25\r\27\2\3\2\7\5\2C\\aac|\3\2\62;")
        buf.write("\3\2$$\4\2\f\f\16\17\4\2\13\13\"\"\2b\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\13\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\3\31\3\2\2\2\5\35\3\2")
        buf.write("\2\2\7\37\3\2\2\2\t\'\3\2\2\2\13*\3\2\2\2\r\66\3\2\2\2")
        buf.write("\178\3\2\2\2\21@\3\2\2\2\23J\3\2\2\2\25R\3\2\2\2\27X\3")
        buf.write("\2\2\2\31\32\7<\2\2\32\4\3\2\2\2\33\36\5\17\b\2\34\36")
        buf.write("\5\13\6\2\35\33\3\2\2\2\35\34\3\2\2\2\36\6\3\2\2\2\37")
        buf.write("$\5\t\5\2 #\5\t\5\2!#\5\r\7\2\" \3\2\2\2\"!\3\2\2\2#&")
        buf.write("\3\2\2\2$\"\3\2\2\2$%\3\2\2\2%\b\3\2\2\2&$\3\2\2\2\'(")
        buf.write("\t\2\2\2(\n\3\2\2\2)+\5\r\7\2*)\3\2\2\2+,\3\2\2\2,*\3")
        buf.write("\2\2\2,-\3\2\2\2-\64\3\2\2\2.\60\7\60\2\2/\61\5\r\7\2")
        buf.write("\60/\3\2\2\2\61\62\3\2\2\2\62\60\3\2\2\2\62\63\3\2\2\2")
        buf.write("\63\65\3\2\2\2\64.\3\2\2\2\64\65\3\2\2\2\65\f\3\2\2\2")
        buf.write("\66\67\t\3\2\2\67\16\3\2\2\28:\7$\2\29;\n\4\2\2:9\3\2")
        buf.write("\2\2;<\3\2\2\2<=\3\2\2\2<:\3\2\2\2=>\3\2\2\2>?\7$\2\2")
        buf.write("?\20\3\2\2\2@D\7%\2\2AC\n\5\2\2BA\3\2\2\2CF\3\2\2\2DB")
        buf.write("\3\2\2\2DE\3\2\2\2EG\3\2\2\2FD\3\2\2\2GH\b\t\2\2H\22\3")
        buf.write("\2\2\2IK\t\6\2\2JI\3\2\2\2KL\3\2\2\2LJ\3\2\2\2LM\3\2\2")
        buf.write("\2MN\3\2\2\2NO\b\n\3\2OP\3\2\2\2PQ\b\n\2\2Q\24\3\2\2\2")
        buf.write("RS\5\27\f\2ST\b\13\4\2TU\3\2\2\2UV\b\13\2\2V\26\3\2\2")
        buf.write("\2WY\7\17\2\2XW\3\2\2\2XY\3\2\2\2YZ\3\2\2\2Z[\7\f\2\2")
        buf.write("[\30\3\2\2\2\r\2\35\"$,\62\64<DLX\5\2\3\2\3\n\2\3\13\3")
        return buf.getvalue()


class LecLexer(LecLexerBase):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INDENT = 1
    DEDENT = 2
    LINE_BREAK = 3
    EQ = 4
    VALUE = 5
    ID = 6
    NUMBER = 7
    STRING = 8
    COMMENT = 9
    WS = 10
    NEWLINE = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'" ]

    symbolicNames = [ "<INVALID>",
            "INDENT", "DEDENT", "LINE_BREAK", "EQ", "VALUE", "ID", "NUMBER", 
            "STRING", "COMMENT", "WS", "NEWLINE" ]

    ruleNames = [ "EQ", "VALUE", "ID", "ALPHA", "NUMBER", "DIGIT", "STRING", 
                  "COMMENT", "WS", "NEWLINE", "RN" ]

    grammarFileName = "LecLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[8] = self.WS_action 
            actions[9] = self.NEWLINE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def WS_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.handle_spaces()
     

    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.handle_new_line()
