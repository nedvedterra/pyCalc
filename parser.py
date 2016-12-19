from . import lex
from . import types
from . import token

import types as stdtypes

class Parser:
    def __init__(self, lexer):
        self.__lexer = lexer 
        self.__lookahead = None 
    def program(self):
        self.__lookahead = self.__lexer.getNextToken()
        result = self.__expr()
        if self.__lookahead.type != types.EOF:
            raise Exception('syntax error: unexpected %s' % self.__lookahead.value)
        else:
            return result
    def __expr(self):
        result = self.__term()
        while self.__lookahead.type in ('+', '-'):
            if self.__lookahead.type == '+':
                self.__match('+')
                result = result + self.__term()
            elif self.__lookahead.type == '-':
                self.__match('-')
                result = result - self.__term()
        return result
    def __term(self):
        result = self.__factor()
        while self.__lookahead.type in ('*', '/', '%', types.INTEGERDIVISION):
            if self.__lookahead.type == '*':
                self.__match('*')
                result = result * self.__factor()
            elif self.__lookahead.type == '/':
                self.__match('/')
                result = result / self.__factor()
            elif self.__lookahead.type == '%':
                self.__match('%')
                result = result % self.__factor()
            elif self.__lookahead.type == types.INTEGERDIVISION:
                self.__match(types.INTEGERDIVISION)
                result = result // self.__factor()
        return result
    def __factor(self):
        result = 0
        if self.__lookahead.type == '+':
            self.__match('+')
            result = +self.__factor()
            return result
        elif self.__lookahead.type == '-':
            self.__match('-')
            result = -self.__factor()
            return result
        else:
            return self.__power()
    def __power(self):
        result = self.__atom_expr()
        if self.__lookahead.type == '^':
            self.__match('^')
            result = result ** self.__factor()
        return result
    def __atom_expr(self):
        result = self.__atom()
        while self.__lookahead.type == '(':
            self.__match('(')
            if type(result) == stdtypes.BuiltinFunctionType:
                result = result(*self.__arglist())
            else:
                result = result * self.__expr()
            self.__match(')')
        return result
    def __arglist(self):
        result = list()
        result.append(self.__expr())
        while self.__lookahead.type == ',':
            self.__match(',')
            result.append(self.__expr())
        return result
    def __atom(self):
        if self.__lookahead.type == '(':
            self.__match('(')
            result = self.__expr()
            self.__match(')')
            return result
        elif self.__lookahead.type == types.IDENTIFIER:
            import math
            result = math.__dict__[self.__lookahead.value]
            self.__match(types.IDENTIFIER)
            return result 
        elif self.__lookahead.type == types.INTEGER:
            result = int(self.__lookahead.value)
            self.__match(types.INTEGER)
            return result
        elif self.__lookahead.type == types.FLOAT:
            result = float(self.__lookahead.value)
            self.__match(types.FLOAT)
            return result
        else:
            raise Exception('syntax error: unexpected %s' % self.__lookahead.value)
    def __match(self, t):
        if self.__lookahead.type == t:
            self.__lookahead = self.__lexer.getNextToken()
        else:
            raise Exception('syntax error: %s expected' % t)
