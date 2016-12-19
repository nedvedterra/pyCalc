class CalcError(Exception):
    def __init__(self, message, index, text):
        self.__message = message
        self.__index = index
        self.__text = text
    def __str__(self):
        result = '%s\n\n%s\n%s' % (self.__message, self.__text,
                                    ' ' * self.__index + '^')
        return result
