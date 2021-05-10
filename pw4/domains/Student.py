
class Student:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob

    def describe(self):
        print(self.__id + " " + self.__name + " " + self.__dob)

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getAvg(self):
        return self.__avg

    def setAvg(self, avg):
        self.__avg = avg
