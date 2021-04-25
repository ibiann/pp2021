# packages
import math
import numpy
import curses
from domains.Student import *
from domains.Course import *
from domains.Mark import *


class InputModule:
    @staticmethod
    def student_num():
        print("==Total number of student==")
        student = int(input("Enter the total: "))
        return studentt

    @staticmethod
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

    @staticmethod
    def course_num():
        print("==Add courses==")
        course = int(input("Enter the total number: "))
        return ()

    @staticmethod
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

    @staticmethod
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
