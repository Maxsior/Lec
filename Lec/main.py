import sys
from antlr4 import *
from LecLexer import LecLexer
from LecParser import LecParser
from LecParserListener import LecParserListener

def print_tree(tree, depth=0):
    indent = ' ' * depth * 4
    if isinstance(tree, TerminalNode):
        print(indent, str(tree.symbol))
    else:
        if isinstance(tree, RuleContext):
            print(indent, tree)
        else:
            print(indent, str(tree.symbol))
        if tree.children:
            for child in tree.children:
                print_tree(child, depth+1)


def main(argv):
    input_stream = FileStream(argv[1], encoding='utf8')
    lexer = LecLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LecParser(stream)
    tree = parser.root()

    extractor = LecParserListener()
    ParseTreeWalker.DEFAULT.walk(extractor, tree)

    # print('*** Tokens ***')
    # for t in stream.tokens:
    #     if t.channel != 1:
    #         print(t)
    #
    # print()
    #
    # print('*** AST ***')
    # print_tree(tree)


if __name__ == '__main__':
    main(sys.argv)
