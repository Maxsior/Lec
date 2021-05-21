lexer grammar LecLexer;

options { superClass=LecLexerBase; }

tokens { INDENT, DEDENT, LINE_BREAK }

EQ : ':' ;

VALUE : (STRING | NUMBER) ;

ID : ALPHA (ALPHA | DIGIT)* ;
fragment ALPHA : [a-zA-Z_] ;

NUMBER : DIGIT+ ('.' DIGIT+)? ;
fragment DIGIT : [0-9] ;

STRING : '"' ~["]+? '"' ;

COMMENT : '#' ~[\r\n\f]* -> channel(HIDDEN);
WS : (' ' | '\t')+ {self.handle_spaces()} -> channel(HIDDEN) ;
NEWLINE : RN {self.handle_new_line()} -> channel(HIDDEN) ;
fragment RN : '\r'? '\n' ;
