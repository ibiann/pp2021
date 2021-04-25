import math
import numpy as np
import curses

Student = []
Studentid = []
Course = []
Courseid = []
Mark = []
Credit = []
Marks_GPA = []

class student:
    def __init__(self, id, name, dob):
        self.studentid = id
        self.student_name = name
        self.student_dob = dob
        Student.append(self)
        Studentid.append(self.studentid)

        def get_id(self):
            return self.Studentid

        def get_name(self):
            return self.student_name

        def get_dob(self):
            return self.student_dob
class course:
    def __init__(self, id, name):
        self.Studentid = id
        self.student_name = name
        self.credit = Credit
        Course.append(self)
        Course.append(self.Studentid)
        Credit.append(self.credit)

    def get_id(self):
        return self.Studentid
    def get_name(self):
        return self.student_name
    def get_credit(self):
        return self.credit

class mark:
    def __init__(self, a, b, mark):
        self.a = a
        self.b = b
        self.mark = mark
        mark.append(self)

    def get_a(self):
        return self.a
    def get_b(self):
        return self.b
    def get_mark(self):
        return self.mark
    def get_GPA(self):
        return self.GPA
def input_information_of_student():
    def input_number_student():
        num = int(input("Enter the numbers of student:"))
        if num <= 0:
            print("There is none!")
            return 0
        else:
            return num
def get_infomation_of_student():
    print("Get info of student to the course:")
    info = {
        'id': '',
        'name': '',
        'dob': ''
    }
    print("Enter Studentid:")
    info['id'] = id = input()
    print("Enter Studentname:")
    info['name'] = input()
    print("Enter date of brith:")
    info['dob'] = input()
    Student.append(info)
    Studentid.append(id)


def get_infomation_of_course():
    print("Number of course")
    number_course = int(input("Enter the number of course:"))
    if (number_course <= 0):
        print("There is no course")
        return 0
    else:
        return number_course

def get_id_of_course():
    name = input("Enter the name of course")
    id = input("Enter the id of course")
    info = {
        'name': name,
        'id': id,
    }
    Course.append(info)
    Courseid.append(id)

def mark():
    def __init__(self,cid,id,mark):
        self.cid=cid
        self.id=id
        self.Mark=mark
        mark.append(self)
    def describe(self):
        print(["Courseid:"], self.cid, ["Studentid:"], self.id, ["mark:"], self.Mark)
    def inputmark():
         print("Enter Course id")
         cid=input()
         if cid in Courseid:
             print("Enter Student id:")
             id=input()
             if id in Studentid:
                 print("Enter the mark:")
                 Mark=float(input())
                 if Mark<0 or Mark >20:
                     print("Wrong")
                     print("Enter mark again")
                     Mark=float(input())
             else:
                 return 0
         else:
             return 0
         Mark(cid,id,Mark)
def average_GPA(self):
    print("___________")
    value=np.array([self.Mark])
    cre=np.array([self.Credit])
    ol=input("Enter the Studentid:")
    if ol in self.id:
        for i in range (len(Mark)):
            GPA=value[i]/cre[i]
            return GPA
    print("Marks_GPA")
def caculate_mark(self):
    print("-----GPA FIND-----")
    id_a=input("Enter the ID:")
    if id_a in self.Studentid:
        mark=input("Enter the mark:")
    mark.append(mark)

    credit_value=[Credit]
    mark_value=[mark]
    name_again=input("Enter name to calculate")
    GPA=mark_value/credit_value
    return GPA

def show_list_student():
    print("----Student List----")
    for i in range(0, len(Student)):
        print(f"ID:{Student[i]['id']} name:{Student[i]['name']} DoB:{Student[i]['dob']}")


def show_list_course():
    print("----Course list----")
    for i in range(0, len(Course)):
        print(f"ID:{Course[i]['id']}  name : {Course[i]['name']}")


def show_mark():
    print("----Student marks list----")
    for i in range(0, len(Mark)):
        print(f"ID-course: {Mark[i]['b']} ID-Student: {Mark[i]['a']}  mark:{Mark[i]['mark']}")

print("choose option")
print("1.y")
print("2.n")
for i in range (0, len(Course)):
    ol=int(input("enter your option:"))
    if ol ==1:
        print("mark of student")
        show_mark()
        break
    else:
        break