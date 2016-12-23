class Token:
    def __init__(self, type, value, index):
        self.__value = value
        self.__type = type
        self.__index = index
    def getData(self):
        return self.__value
    def getType(self):
        return self.__type
    def getIndex(self):
        return self.__index
    value = property(getData)
    type = property(getType)
    index = property(getIndex)
