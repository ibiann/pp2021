import math

from pp2021.pw4.output import calculateAvg

# Add Information
def InputinfoStudent(students):
    id = input("Enter Id: ")
    name = input("Enter Name: ")
    dob = input("Enter dob: ")
    student = Student.Student(id, name, dob)
    students.append(student)

# Add Course Info
def InputinfoCourse(courses):
    id = input("Enter Id: ")
    name = input("Enter name: ")
    credit = input("Enter credit: ")
    course = Course.Course(id, name, credit)
    courses.append(course)

# Marks information
def inputMark(courses, students, studentMark):
    courseName = input("Enter name of course for the mark: ")
    for c in courses:
        if c.getName() == courseName:
            for s in students:
                mark = math.floor(float(input("Input " + s.getName() + "'s mark: ")))
                studentMark = StudentMark(s, c, mark)
                studentMarks.append(studentMark)
                s.setAvg(calculateAvg(s.getId()))