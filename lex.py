from . import token
from . import types
from . import patterns
import re
class Lex:
    def __init__(self, text = ''):
        self.__text = text 
        self.__currentIndex = 0 
        self.__generator = self.__genTokens()
    def __iter__(self):
        return self.__generator
    def __findToken(self, type, pattern):
        result = re.match(pattern, self.__text[self.__currentIndex:])
        if result:
            tk = token.Token(type, result.group(), self.__currentIndex)
            self.__currentIndex += result.end()
            return tk
        else:
            return None
    def __genTokens(self):
        while self.__currentIndex < len(self.__text):
            for type, pattern in patterns.PATTERNS:
                tk = self.__findToken(type, pattern)
                if tk:
                    if type != types.WHITESPACE:
                        yield tk
                    break
            else:
                raise Exception('syntax error: character %s' % self.__currentIndex,
                                self.__text)         

    def getNextToken(self):
        return next(self.__generator)
    def reset(self):
        self.__init__(self.text)
    def getText(self):
        return self.__text
    def setText(self, text):
        self.__init__(text)
    text = property(getText, setText)
