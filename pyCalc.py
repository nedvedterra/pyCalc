from .interpreter import parser, lex, exceptions

class PyCalc:
    def __init__(self):
        self.__lexer = lex.Lex()
        self.__parser = parser.Parser(self.__lexer)
    def compute(self, text):
        self.__lexer.text = text 
        result = None
        try:
            result = self.__parser.program()
        except exceptions.CalcError as E:
            print('%s: %s' % (E.__class__.__name__, str(E)))
        return result

calculator = PyCalc()
