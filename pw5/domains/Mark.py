
class StudentMark:
    def __init__(self, student, course, mark):
        self.__student = student
        self.__course = course
        self.__mark = mark

    def getStudent(self):
        return self.__student

    def getCourse(self):
        return self.__course

    def getMark(self):
        return self.__mark

    def describe(self):
        print(self.__student.getId() + " " + self.__student.getName() + " "
              + self.__course.getName() + " " + str(self.__mark))
