students = []
studentID = []
studentName = []
studentDoB = []

class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        Student.append(self)
        Student.append(self.id)

    def describe(self):
        print(self.id + " " + self.name + " " + self.dob)

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getdob(self):
        return self.dob

    def getAvg(self):
        return self.avg

    def setAvg(self, avg):
        self.avg = avg
