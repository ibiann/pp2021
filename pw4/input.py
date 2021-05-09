from domains import Student, Course, Mark
import math


def AddinforStudent(students):
    id = input("Enter Id: ")
    name = input("Enter Name: ")
    dob = input("Enter dob: ")
    students = Student(id, name, dob)
    students.append(students)

def AddinforCourse(courses):
    id = input("Enter Id: ")
    name = input("Enter name: ")
    credit = input("Enter credit: ")
    courses = Course(id, name, credit)
    courses.append(courses)

def inputMark(courses, students, studentMarks):
    courseName = input("Input course's name to input marks: ")
    for c in courses:
        if c.getName() == courseName:
            for s in students:
                mark = math.floor(float(input("Input " + s.getName() + "'s mark: ")))
                studentMark = StudentMark.StudentMark(s, c, mark)
                studentMarks.append(studentMark)
                s.setAvg(calculateAvg(s.getId(), studentMarks))