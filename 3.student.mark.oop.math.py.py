import math
import numpy as np
import curses

#
Student = []
StudentID = []
Course = []
CourseID = []
Mark = []
Credit = []
Mark_GPA = []


class Students:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
        Student.append(self)
        StudentID.append(self.__id)

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_dob(self):
        return self.student.dob


class Courses:
    def __init__(self, cid, cname, ccredit):
        self.Cid = cid
        self._cname = cname
        self.ccredit = ccredits
        Course.append(self)
        CourseID.append(self.Cid)
        Credit.append(self._ccredit)

    def get_id(self):
        return self.Cid

    def get_name(self):
        return self.Cname

    def get_credit(self):
        return self.Ccredit


class Marks:
    def __init__(self, x, y, mark, gpa):
        self.x = x
        self.y= y
        self._mark = mark
        Mark.append(self)

    def get_mid(self):
        return self.x

    def get_nid(self):
        return self.y

    def get_mark(self):
        return self.mark

    def get_gpa(self):
        return self.gpa


# Input total number of students
def student_num():
    print("==Total number of student==")
    student = int(input("Enter the total: "))
    return student

# Add student
def add_student():
    print("==Add student==")
    id = input("Enter ID: ")
    name = input("Enter NAME: ")
    dob = input("Enter DOB: ")
    st_u = {
        'id': id,
        'name': name,
        'dob': dob
    }
    Student.append(st_u)
    StudentID.append(id)


# Add number of course
def course_num():
    print("==Add courses==")
    course = int(input("Enter the total number: "))
    return()


# Add course
def add_course():
    print("---- ADD A COURSE ----")
    Cid = input("Enter ID: ")
    Cname = input("Enter name: ")
    CC = input("Enter Credit: ")
    Cr_o = {
        'cid': cid,
        'cname': cname,
        'cc': cc
    }
    Course.append(Cr_o)
    CourseID.append(Cid)


# Create mark for students
def create_mark():
    g = 1
    tu = len(Student)
    while g <= tu:
        g += 1
        x = input("Enter Student ID: ")
        if x in Student:
            for i in range(0, len(CourseID)):
                y = input("Enter Course ID: ")
                if y in CourseID:
                    mark = float(input("Enter Student mark: "))
                    kk = {
                        'mid': x,
                        'nid': y,
                        'mark': mark
                    }
                else:
                    print("Sid NOT FOUND !!")
                    break
                Mark.append(kk)
        else:
            print("Cid NOT FOUND !!")
            break


def mark_gpa():
    null = numpy.array([self._ccredit])
    strace.addstr("Enter Student ID:")
    id = strace.getstr().decode()
    if id in StudentID:
        for i in range(0, len(Student)):
            marktotal = numpy.sum(null)
            gpatotal = numpy.sum(numpy.multiply(int, null))
            strace.refresh()
            gpa = gpatotal / marktotal
            strace.refresh()

    else:
        return 0
    print(gpa)

    MarkGPA.append(gpa)
    strace.refresh()
    for point in Mark:
        strace.clear()
        strace.refresh()
        strace.addstr(" [Mark: ] %s   [GPA: ]%s \n" % (mark.get_id(), gpa))
        break


def gpa_sort():
    sor_tg = numpy.array([MarkGPA])
    sor_tg[::-1].sort()
    strace.addstr("GPA sorted %s: \n" % sor_tg)
    strace.refresh()


def show_list_student():
    print("**Student list**")
    for i in range(0, len(Student)):
        print(f"ID:{Student[i]['id']} name:{Student[i]['name']} DoB:{Student[i]['dob']}")


def show_list_course():
    print("**Course list**")
    for i in range(0, len(Course)):
        print(f"ID:{Course[i]['id']}  name : {Course[i]['name']}")


def show_mark():
    print("**Mark list**")
    for i in range(0, len(Mark)):
        print(f"ID-course: {Mark[i]['b']} ID-Student: {Mark[i]['a']}  mark:{Mark[i]['mark']}")


# main
s = int(student_num())
l = 1
while l <= s:
    l += 1
    add_student()
    show_list_student()

c = int(course_num())
p = 1
while p <= c:
    p += 1
    add_course()
    show_list_course()

# GPA
mark_gpa()


create_mark()
for i in range(0, len(Course)):
    ol = int(input("You Choose: "))
    if ol == 1:
        print("**Mark**")
        show_mark()
        break
    else:
        break