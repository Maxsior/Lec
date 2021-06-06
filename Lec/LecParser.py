# Generated from .\LecParser.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("\61\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\7\2\16")
        buf.write("\n\2\f\2\16\2\21\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\4\6\4 \n\4\r\4\16\4!\3\4\3\4\3\4\5")
        buf.write("\4\'\n\4\3\5\3\5\6\5+\n\5\r\5\16\5,\3\5\3\5\3\5\2\2\6")
        buf.write("\2\4\6\b\2\3\3\2\7\b\2\62\2\17\3\2\2\2\4\24\3\2\2\2\6")
        buf.write("&\3\2\2\2\b(\3\2\2\2\n\16\7\5\2\2\13\16\5\4\3\2\f\16\5")
        buf.write("\6\4\2\r\n\3\2\2\2\r\13\3\2\2\2\r\f\3\2\2\2\16\21\3\2")
        buf.write("\2\2\17\r\3\2\2\2\17\20\3\2\2\2\20\22\3\2\2\2\21\17\3")
        buf.write("\2\2\2\22\23\7\2\2\3\23\3\3\2\2\2\24\25\7\b\2\2\25\26")
        buf.write("\7\6\2\2\26\27\7\5\2\2\27\30\7\3\2\2\30\31\5\6\4\2\31")
        buf.write("\32\7\4\2\2\32\5\3\2\2\2\33\34\7\b\2\2\34\35\7\5\2\2\35")
        buf.write("\37\7\3\2\2\36 \5\6\4\2\37\36\3\2\2\2 !\3\2\2\2!\37\3")
        buf.write("\2\2\2!\"\3\2\2\2\"#\3\2\2\2#$\7\4\2\2$\'\3\2\2\2%\'\5")
        buf.write("\b\5\2&\33\3\2\2\2&%\3\2\2\2\'\7\3\2\2\2(*\7\b\2\2)+\t")
        buf.write("\2\2\2*)\3\2\2\2+,\3\2\2\2,*\3\2\2\2,-\3\2\2\2-.\3\2\2")
        buf.write("\2./\7\5\2\2/\t\3\2\2\2\7\r\17!&,")
        return buf.getvalue()


class LecParser ( Parser ):

    grammarFileName = "LecParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "':'" ]

    symbolicNames = [ "<INVALID>", "INDENT", "DEDENT", "LINE_BREAK", "EQ", 
                      "VALUE", "ID", "NUMBER", "STRING", "COMMENT", "WS", 
                      "NEWLINE" ]

    RULE_root = 0
    RULE_variable = 1
    RULE_obj = 2
    RULE_obj_call = 3

    ruleNames =  [ "root", "variable", "obj", "obj_call" ]

    EOF = Token.EOF
    INDENT=1
    DEDENT=2
    LINE_BREAK=3
    EQ=4
    VALUE=5
    ID=6
    NUMBER=7
    STRING=8
    COMMENT=9
    WS=10
    NEWLINE=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(LecParser.EOF, 0)

        def LINE_BREAK(self, i:int=None):
            if i is None:
                return self.getTokens(LecParser.LINE_BREAK)
            else:
                return self.getToken(LecParser.LINE_BREAK, i)

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LecParser.VariableContext)
            else:
                return self.getTypedRuleContext(LecParser.VariableContext,i)


        def obj(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LecParser.ObjContext)
            else:
                return self.getTypedRuleContext(LecParser.ObjContext,i)


        def getRuleIndex(self):
            return LecParser.RULE_root

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoot" ):
                listener.enterRoot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoot" ):
                listener.exitRoot(self)




    def root(self):

        localctx = LecParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LecParser.LINE_BREAK or _la==LecParser.ID:
                self.state = 11
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 8
                    self.match(LecParser.LINE_BREAK)
                    pass

                elif la_ == 2:
                    self.state = 9
                    self.variable()
                    pass

                elif la_ == 3:
                    self.state = 10
                    self.obj()
                    pass


                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
            self.match(LecParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LecParser.ID, 0)

        def EQ(self):
            return self.getToken(LecParser.EQ, 0)

        def LINE_BREAK(self):
            return self.getToken(LecParser.LINE_BREAK, 0)

        def INDENT(self):
            return self.getToken(LecParser.INDENT, 0)

        def obj(self):
            return self.getTypedRuleContext(LecParser.ObjContext,0)


        def DEDENT(self):
            return self.getToken(LecParser.DEDENT, 0)

        def getRuleIndex(self):
            return LecParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = LecParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(LecParser.ID)
            self.state = 19
            self.match(LecParser.EQ)
            self.state = 20
            self.match(LecParser.LINE_BREAK)
            self.state = 21
            self.match(LecParser.INDENT)
            self.state = 22
            self.obj()
            self.state = 23
            self.match(LecParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LecParser.ID, 0)

        def LINE_BREAK(self):
            return self.getToken(LecParser.LINE_BREAK, 0)

        def INDENT(self):
            return self.getToken(LecParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(LecParser.DEDENT, 0)

        def obj(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LecParser.ObjContext)
            else:
                return self.getTypedRuleContext(LecParser.ObjContext,i)


        def obj_call(self):
            return self.getTypedRuleContext(LecParser.Obj_callContext,0)


        def getRuleIndex(self):
            return LecParser.RULE_obj

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObj" ):
                listener.enterObj(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObj" ):
                listener.exitObj(self)




    def obj(self):

        localctx = LecParser.ObjContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_obj)
        self._la = 0 # Token type
        try:
            self.state = 36
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.match(LecParser.ID)
                self.state = 26
                self.match(LecParser.LINE_BREAK)
                self.state = 27
                self.match(LecParser.INDENT)
                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 28
                    self.obj()
                    self.state = 31 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==LecParser.ID):
                        break

                self.state = 33
                self.match(LecParser.DEDENT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.obj_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Obj_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(LecParser.ID)
            else:
                return self.getToken(LecParser.ID, i)

        def LINE_BREAK(self):
            return self.getToken(LecParser.LINE_BREAK, 0)

        def VALUE(self, i:int=None):
            if i is None:
                return self.getTokens(LecParser.VALUE)
            else:
                return self.getToken(LecParser.VALUE, i)

        def getRuleIndex(self):
            return LecParser.RULE_obj_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObj_call" ):
                listener.enterObj_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObj_call" ):
                listener.exitObj_call(self)




    def obj_call(self):

        localctx = LecParser.Obj_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_obj_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(LecParser.ID)
            self.state = 40 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 39
                _la = self._input.LA(1)
                if not(_la==LecParser.VALUE or _la==LecParser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 42 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==LecParser.VALUE or _la==LecParser.ID):
                    break

            self.state = 44
            self.match(LecParser.LINE_BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
