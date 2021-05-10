
class Course:
    def __init__(self, id, name, credit):
        self.__id = id
        self.__name = name
        self.__credit = credit

    def describe(self):
        print("Id: " + self.__id + " Course name: " + self.__name + " credit: " + self.__credit)

    def getName(self):
        return self.__name

