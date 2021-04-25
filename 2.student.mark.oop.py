# Student management

Students=[]
StudentID=[]
Courses=[]
CoursesID=[]
Mark=[]

class  Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        Students.append(self)
        StudentID.append(self.id)

    def get_id(self):
        return self.studentid

    def get_name(self):
        return self.student_name

    def get_dob(self):
        return self.student_dob

class course():
    print("===Add course===")
    x = input("Enter CID: ")
    cname = input("Enter CNAME: ")
    cc = input("Enter CCredit:")
    cr_o = {
        'cid': x,
        'cname': cname,
        'cc': cc
    }
    Course.append(cr_o)
    CourseID.append(x)

class mark():
    def __init__(self, x, y, marks):
        self.x = x
        self.y = y
        self.marks = marks
        Mark.append(self)

    def get_mid(self):
        return self.x

    def get_nid(self):
        return self.y

    def get_mark(self):
        return self.mark

    def get_gpa(self):
        return self.gpa

     def inputStudent():
         print("ADD STUDENT OF THIS COURSES:")
         print("Enter StudentID:")
         id = input()
         print("Enter StudentName:")
         name = input()
         print("Enter date of brith:")
         dob = input()
         Student(id, name, dob)


     def inputMark():
         print("Enter Courses id")
         cid = input()
         if cid in CoursesID:
             print("Enter Student ID:")
             id = input()
             if id in StudentID:
                 print("Entrer marks:")
                 marks = float(input())
                 if marks < 0 or marks > 20:
                     print("Error")
                     print("Enter marks again")
                     marks = float(input())
             else:
                 return 0
         else:
             return 0
         mark(cid, id, marks)



     def StudentManagement():
         print("*************************")
         print("""please select an option:
         1.  Input  Courses:
         2.  Stop """)
         option=int(input("Choose:"))
         if option==1:
             Nco=Course.input_number_courses()
             print("1.Add course:")
             print("2.End: ")
             option1=int(input("Choose:"))
             if option1==1:
                 for i in range( Nco):
                     Course.inputCourses()
                     Num=Student.input_number_student()
                     for i in range(Num):
                         print("1. Input Student:")
                         print("2. End:")
                         option2=int(input("Choose:"))
                         if option2==1:
                             for i in range(Num):
                                 Student.inputStudent()
                                 Start.ShowCourses()
                                 Start.ShowStudent()
                                 print("1. Add marks:")
                                 print("2. End:")
                                 option3=int(input("Choose:"))
                                 if option3==1:
                                     mark.inputMark()
                                     Start.ShowCourses()
                                     Start.ShowStudent()
                                     Start.ShowMarks()
                                     break
                                 else:
                                   exit()
                         else:
                            exit()
             else:
               exit()
         else:
             print("The end: ")
             exit()
Start.ShowMarks()
Start.StudentManagement()
