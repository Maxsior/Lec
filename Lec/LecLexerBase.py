from antlr4 import *
from antlr4.Token import CommonToken

import LecLexer


class LecLexerBase(Lexer):
    _default_indent_size = -1
    _indents = []
    _prev_token: Token = None
    _tokens = []
    _emited = False

    def nextToken(self):
        self._emited = False
        if self._tokens:
            next_ = self._tokens.pop(0)
        else:
            next_ = super().nextToken()

            if next_.type == Token.EOF:
                self._emited = True
                self._handle_eof()
                self.emitToken(next_)
                next_ = self._tokens.pop(0)
        return next_

    def handle_new_line(self):
        self.emit_type(LecLexer.LecLexer.NEWLINE, self.HIDDEN)

        next_ = self._input.LA(1)
        if next_ == Token.EOF:
            self._handle_eof()
            return

        next_char = chr(next_)

        if not self.is_indent(next_char) and not self.is_newline_or_comment(next_char):
            self._process_new_line(0)

    def handle_spaces(self):
        next_ = self._input.LA(1)
        if next_ == Token.EOF:
            self._handle_eof()
            return

        next_char = chr(next_)

        if (
                (self._prev_token is None or self._prev_token.type == LecLexer.LecLexer.NEWLINE) and
                not self.is_newline_or_comment(next_char)
        ):
            indent_size = len(self.text)

            if self._default_indent_size == -1:
                self._default_indent_size = indent_size

            if indent_size % self._default_indent_size != 0:
                raise RecognitionException("Mixed indent size", self, self._input)

            self._process_new_line(indent_size)

        else:
            self.emit_type(LecLexer.LecLexer.WS, self.HIDDEN, self.text)

    def _process_new_line(self, indent):
        self.emit_type(LecLexer.LecLexer.LINE_BREAK)

        previous = self._indents[-1] if self._indents else 0

        if indent > previous:
            self._indents.append(indent)
            self.emit_type(LecLexer.LecLexer.INDENT)
        else:
            while self._indents and self._indents[-1] > indent:
                self.emit_type(LecLexer.LecLexer.DEDENT)
                self._indents.pop()

    def emit_type(self, token_type, channel=Token.DEFAULT_CHANNEL, text=""):
        char_index = self.getCharIndex()
        token = CommonToken(self._tokenFactorySourcePair, token_type, channel, char_index - len(text), char_index)
        token.line = self.line
        token.column = self.column
        token.text = text

        self.emitToken(token)
        return token

    def emitToken(self, token):
        if not self._emited:
            self._emited = True
            super().emitToken(token)
            self._prev_token = token
        else:
            self._tokens.append(token)

    def is_indent(self, char):
        return char == ' ' or char == '\t'

    def is_newline_or_comment(self, char):
        return char == '\r' or char == '\n' or char == '\f' or char == '#'

    def _handle_eof(self):
        self.emit_type(LecLexer.LecLexer.LINE_BREAK)
        while self._indents:
            self._indents.pop()
            self.emit_type(LecLexer.LecLexer.DEDENT)
