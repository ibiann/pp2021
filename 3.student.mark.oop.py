# Student management
#------------------------------------list-----------------------------------#
Students=[]
StudentID=[]
Courses=[]
CoursesID=[]
Mark=[]
#-----------------------------------Student-----------------------------#
class  Student:
    def __init__(self,id,name,dob):
        self.id=id
        self.name=name
        self.dob=dob
        Students.append(self) 
        StudentID.append(self.id)
    def describe(self):
        print(["id:"],self.id, ["name:"],self.name, ["dob:"],self.dob)
    
    
    def input_number_student():
         Num=int(input("Enter the numbers of Student:"))
         if Num <=0:
             print("Does not exist!!!")
             return 0
         else:
             return Num
    def inputStudent():
         print("ADD STUDENT OF THIS COURSES:")
         print("Enter StudentID:")
         id=input()
         print("Enter StudentName:")
         name=input()
         print("Enter date of brith:")
         dob=input()
         Student(id,name,dob)
    
#-----------------------------------------Course------------------------------#
class Course:
    def __init__(self,cid,name):
        self.cid=cid
        self.name=name
        Courses.append(self)
        CoursesID.append(self.cid)
    def describe(self):
        print(["cid:"],self.cid , ["name:"],self.name)
    def input_number_courses():
         Nco=int(input("Enter the numbers of course:"))
         if Nco<=0:
            print("Does not exist!!!")
            return 0
         else:
             return Nco
    def inputCourses():
         print("ADD COURSES:")
         print("Enter CoursesID:")
         cid=input()
         print("Enter CoursesName:")
         name=input()
         Course(cid,name)
#-------------------------------------------Mark------------------------------------#
class mark:
    def __init__(self,cid,id,marks):
        self.cid=cid
        self.id=id
        self.marks=marks
        Mark.append(self)
    def describe(self):
        print(["Coursesid:"],self.cid, ["Studentid:"],self.id, ["mark:"],self.marks)
    def inputMark():
         print("Enter Courses id")
         cid=input()
         if cid in CoursesID:
             print("Enter Student ID:")
             id=input()
             if id in StudentID:
                 print("Entrer marks:")
                 marks=float(input())
                 if marks<0 or marks >20:
                     print("Error")
                     print("Enter marks again")
                     marks=float(input())
             else:
                 return 0
         else:
             return 0
         mark(cid,id,marks)
       
#--------------------------------------Show--------------------------------# 
class Start:
     def ShowCourses():
         print("Show lists of courses:")
         for i in range(0,len(Courses)):
             print("[",Course.describe(Courses[i]),"]",)
     def ShowStudent():
         print("Show lists of Student:")
         for i in range(0,len(Students)):
             print("[",Student.describe(Students[i]),"]",)
     def ShowMarks():
          print("Show marks of Student in courses:")
          for i in range(len(Students)):  
              print("[",mark.describe(Mark[i]),"]",)
#-------------------------------------Main--------------------------------------#
     def StudentManagement():  
         print("*************************")
         print("""please select an option form list:
         1.  Input  Courses:
         2.  Stop """)
         option=int(input("YOU CHOOSE:"))
         if option==1:
             Nco=Course.input_number_courses()
             print("1.ADD COURSES:")
             print("2.Stop")
             option1=int(input("YOU CHOOSE:"))
             if option1==1:
                 for i in range( Nco):
                     Course.inputCourses()
                     Num=Student.input_number_student()
                     for i in range(Num):
                         print("1. INPUT  STUDENT:")
                         print("2.Stop:")
                         option2=int(input("YOU CHOOSE:"))
                         if option2==1:
                             for i in range(Num):
                                 Student.inputStudent()
                                 Start.ShowCourses()
                                 Start.ShowStudent()
                                 print("1.ADD marks:")
                                 print("2.Stop:")
                                 option3=int(input("YOU CHOOSE:"))
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
             print("Good bye:")
             exit()
Start.ShowMarks()
Start.StudentManagement()
