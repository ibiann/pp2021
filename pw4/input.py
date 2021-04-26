# packages
import math
import numpy
import curses
from domains.Student import *
from domains.Course import *
from domains.Mark import *


class InputModule:
    # Input total number of students
    @staticmethod

    def student_num():
        print("**Total Students**")
        student = int(input("Enter total number of student: "))
        return student

# Add student

    print("**Add student**")
    id = input("Id: ")
    Name = input("Name: ")
    dob = input("DOB: ")
    student = Student(id, Name, dob)
    Student.append(student)
    Student.append(self.id)

# Add course
    @staticmethod
    def add_Course():
        print("**Add course**")
        id = input("id: ")
        name = input("name: ")
        credit = input("credit: ")
        course = Course(id, name, credit)
        Courses.append(course)

# Add mark
    @staticmethod
def Add_Mark():
    courseName = input("Enter the Mark of the courses: ")
    for C in Courses:
        if C.getName() == courseName:
            for S in Student:
                Mark = math.floor(float(input("Enter " + S.getName() + "'S Mark: ")))
                StudentMark = Marks(S, C, Mark)
                StudentMarks.append(StudentMark)
                S.setAvg(calculateAvg(S.getId()))
