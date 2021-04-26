import numpy
import curses
from domains.Student import *
from domains.Course import *
from domains.Mark import *

class OutputModule:
    @staticmethod
    def ShowlistCourses():
        print("Show course list:")
        for c in Courses:
            c.describe()

    @staticmethod
    def ShowlistStudents():
        print("Show student list:")
        for s in Student:
            s.describe()

    @staticmethod
    def ShowMarks():
        courseName = input("Enter the name of course to show mark: ")
        print("Marks " + courseName)
        for StudentMark in StudentMarks:
            if courseName == StudentMark.getCourse().getName():
                StudentMark.describe()

    @staticmethod
    def Show_Average():
        id = input("Enter student's id: ")
        for s in Student:
            if id == s.getId():
                print("Name: " + s.getName() + " Avg: " + str(s.getAvg()))