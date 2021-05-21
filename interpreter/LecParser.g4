parser grammar LecParser;

options { tokenVocab=LecLexer; }

root : (LINE_BREAK | variable | obj)* EOF ;

variable: ID EQ LINE_BREAK INDENT obj DEDENT ;

obj : ID LINE_BREAK INDENT obj+ DEDENT | obj_call ;

obj_call : ID (VALUE | ID)+ LINE_BREAK ;
