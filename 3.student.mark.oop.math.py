"""
@Author: Pham Chi Trung
@ID: BA9-065
@Lab work 3
"""
import math
import numpy

students = []
courses = []
studentsMarks = []

# Add student
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

# Add Course
class Course:
    def __init__(self, id, name, credit):
        self.__id = id
        self.__name = name
        self.__credit = credit

    def describe(self):
        print("Id: " + self.__id + " Course name: " + self.__name + " credit: " + self.__credit)

    def getName(self):
        return self.__name

# Add Mark
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

# Add Information
def AddInforStudent():
    id = input("Enter Id: ")
    name = input("Enter Name: ")
    dob = input("Enter dob: ")
    student = Student(id, name, dob)
    students.append(student)

# Add Course Info
def AddInforCourse():
    id = input("Enter Id: ")
    name = input("Enter name: ")
    credit = input("Enter credit: ")
    course = Course(id, name, credit)
    courses.append(course)

# Marks information
def inputMark():
    courseName = input("Input course's name to input marks: ")
    for c in courses:
        if c.getName() == courseName:
            for s in students:
                mark = math.floor(float(input("Input " + s.getName() + "'s mark: ")))
                studentMark = StudentMark(s, c, mark)
                studentMarks.append(studentMark)
                s.setAvg(calculateAvg(s.getId()))

# Display
def ShowlistCourses():
    print("Show course List:")
    for c in courses:
        c.describe()


def ShowlistStudents():
    print("Show student List:")
    for s in students:
        s.describe()


def ShowMarks():
    courseName = input("Enter name of course to show marks: ")
    print("Student Marks for " + courseName)
    for studentMark in studentMarks:
        if courseName == studentMark.getCourse().getName():
            studentMark.describe()

# Average Calculation
def calculationAvg(id):
    marks = []
    for studentMark in studentMarks:
        if (studentMark.getStudent().getId() == id):
            marks.append(studentMark.getMark())
    return numpy.average(marks)



def showAvarage():
    id = input("Input student id: ")
    for s in students:
        if id == s.getId():
            print("Name: " + s.getName() + " Avg: " + str(s.getAvg()))

def sortAvg():
    sortedList = sorted(students, key=lambda x: x.gpa, reverse=True)
    for s in sortedList:
        s.describe()

def calculationWeightedSum(id):
    sum = 0
    for c in courses:
        smark = []
        warray = []
        for studentMark in studentMarks:
            if (studentMark.getStudent().getId == id):
                smark.append(studentMark.getMark())
                warray.append(c.etc)
        weights = numpy.array(warray)
        amark = numpy.array(smark)
        sum = sum + numpy.sum(numpy.dot(amark, weights))
    return sum

def showWeightedSum():
    id = input("Input student id: ")
    print("Weighted sum: " + str(calculateWeightedSum(id)))


# Main
def menu():
    option = "-1";
    while (option != "0"):
        print("""
                   MENU
            1. Add students
            2. Add courses
            3. Add marks
            4. Show student list
            5. Show course list
            6. Show mark list
            7. Calculate average score
            8. Calculate weighted sum
            9. Sort student list
            0. Exit
            """)
        option = input("Your option: ")
        if (option == "1"):
            AddInforStudent()
        elif (option == "2"):
            AddInforCourse()
        elif (option == "3"):
            inputMark()
        elif (option == "4"):
            ShowlistStudents()
        elif (option == "5"):
            ShowlistCourses()
        elif (option == "6"):
            ShowMarks()
        elif (option == "7"):
            showAvarage()
        elif (option == "8"):
            showWeightedSum();
        elif (option == "9"):
            sortAvg();

menu()
print("The program has ended")