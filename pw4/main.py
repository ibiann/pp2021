import curses
from output import OutputModule
from input import InputModule
from domains.Student import *
from domains.Course import *
from domains.Mark import *

class MainModule:
    def menu():
        option = "-1";
        while (option != "0"):
            print("""
                1. Add students
                2. Add courses
                3. Add marks
                4. Show student list
                5. Show course list
                6. Show mark list
                7. Calculate average score
                8. Calculate weighted sum
                9. Sort student list
                0. Exit
                """)
            option = input("You option: ")
            if (option == "1"):
                add_student()
            elif (option == "2"):
                add_Course()
            elif (option == "3"):
                Add_Mark()
            elif (option == "4"):
                ShowlistStudents()
            elif (option == "5"):
                ShowlistCourses()
            elif (option == "6"):
                ShowMarks()
            elif (option == "7"):
                Show_Average()
            elif (option == "8"):
                WeightedSumShow()
            elif (option == "9"):
                sortbyAvg();

    menu()
    print("End of program")