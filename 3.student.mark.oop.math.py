"""
@Author: Pham Chi Trung
@ID: BA9-065
@Lab work 3
"""

import math
import numpy
import curses

Student = []
Courses = []
StudentMarks = []
GPA = []
Mark_GPA = []
Credit = []
CoursesId = []

screen = curses.initscr()
print("Approved")
screen.refresh()
curses.napms(3000)
curses.endwin()
print("Ended")

#Add information

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


class Course:
    def __init__(self, Cid,Cname,Ccredit):
        self.Cid = Cid
        self.Cname = Cname
        self.Ccredit = Ccredit

    def describe(self):
        print("Id: " + self.Cid + " Course name: " + self.Cname + " credit: " + self.Ccredit)

    def getName(self):
        return self.Cname


class Marks:
    def __init__(self, Student, Courses, Marks):
        self.student = Student
        self.course = Courses
        self.mark = Marks

    def getStudent(self):
        return self.student

    def getCourse(self):
        return self.course

    def getMark(self):
        return self.mark

    def describe(self):
        print(self.student.getId() + " " + self.student.getName() + " "
              + self.course.getName() + " " + str(self.mark))

# Input total number of students

def student_num():
    print("**Total Students**")
    student = int(input("Enter total number of student: "))
    return student

# Add Student

def add_student():
    print("**Add student**")
    id = input("Id: ")
    Name = input("Name: ")
    dob = input("DOB: ")
    student = Student(id, Name, dob)
    Student.append(student)
    Student.append(self.id)

# Add course

def add_Course():
    print("**Add course**")
    id = input("id: ")
    name = input("name: ")
    credit = input("credit: ")
    course = Course(id, name, credit)
    Courses.append(course)

# Add mark

def Add_Mark():
    courseName = input("Enter the Mark of the courses: ")
    for C in Courses:
        if C.getName() == courseName:
            for S in Student:
                Mark = math.floor(float(input("Enter " + S.getName() + "'S Mark: ")))
                StudentMark = Marks(S, C, Mark)
                StudentMarks.append(StudentMark)
                S.setAvg(calculateAvg(S.getId()))

# Display
def ShowlistCourses():
    print("Show course list:")
    for c in Courses:
        c.describe()


def ShowlistStudents():
    print("Show student list:")
    for s in Student:
        s.describe()


def ShowMarks():
    courseName = input("Enter the name of course to show mark: ")
    print("Marks " + courseName)
    for StudentMark in StudentMarks:
        if courseName == StudentMark.getCourse().getName():
            StudentMark.describe()

# Average Calculation
def Avg_calulation(id):
    marks = []
    for Studentmark in StudentMarks:
        if (Studentmark.getStudent().getId() == id):
            marks.append(Studentmark.getMark())
    return numpy.average(marks)

# Result of Avarage

def Show_Average():
    id = input("Enter student's id: ")
    for s in Student:
        if id == s.getId():
            print("Name: " + s.getName() + " Avg: " + str(s.getAvg()))

def sortbyAvg():
    sortedList = sorted(Student, key=lambda x: x.GPA, reverse=True)
    for s in sortedList:
        s.describe()

# WeightSum Calculation
def WeightedSumCalculation(id):
    sum = 0
    for c in Courses:
        Smark = []
        Warray = []
        for studentMark in StudentMarks:
            if (studentMark.getStudent().getId == id):
                Smark.append(studentMark.getMark())
                Warray.append(c.etc)
        weights = numpy.array(Warray)
        amark = numpy.array(Smark)
        sum = sum + numpy.sum(numpy.dot(amark, weights))
    return sum

# Show result of WeightedSum
def WeightedSumShow():

    Sid = input("Enter student's id: ")
    print("Weighted sum: " + str(calculateWeightedSum(id)))

# Main
def menu():
    option = "-1";
    while (option != "0"):
        print("""
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
        option = input("You option: ")
        if (option == "1"):
            add_student()
        elif (option == "2"):
            add_Course()
        elif (option == "3"):
            Add_Mark()
        elif (option == "4"):
            ShowlistStudents()
        elif (option == "5"):
            ShowlistCourses()
        elif (option == "6"):
            ShowMarks()
        elif (option == "7"):
            Show_Average()
        elif (option == "8"):
           WeightedSumShow()
        elif (option == "9"):
            sortbyAvg();

menu()
print("End of program")