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