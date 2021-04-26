import numpy
import math

def AddInforStudent():
    id = input("Enter Id: ")
    name = input("Enter Name: ")
    dob = input("Enter dob: ")
    student = Student(id, name, dob)
    students.append(student)

def AddInforCourse():
    id = input("Enter Id: ")
    name = input("Enter name: ")
    credit = input("Enter credit: ")
    course = Course(id, name, credit)

def inputMark():
    courseName = input("Input course's name to input marks: ")
    for c in courses:
        if c.getName() == courseName:
            for s in students:
                mark = math.floor(float(input("Input " + s.getName() + "'s mark: ")))
                studentMark = StudentMark(s, c, mark)
                studentMarks.append(studentMark)
                s.setAvg(calculateAvg(s.getId()))