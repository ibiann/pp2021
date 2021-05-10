import input as input
import output

students = []
studentsMarks = []
courses = []

def menu():
    option = "-1";
    while (option != "0"):
        print("""
                   MENU
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
        option = input("Your option: ")
        if (option == "1"):
            input.InputinfoStudent(students)
        elif (option == "2"):
            input.InputinfoCourse(courses)
        elif (option == "3"):
            input.inputMark(courses, students, studentsMarks)
        elif (option == "4"):
            input.showlistStudent(students)
        elif (option == "5"):
            input.ShowlistCourses(courses)
        elif (option == "6"):
            input.ShowMarks(studentsMarks)
        elif (option == "7"):
            input.showAvarage(students)
        elif (option == "8"):
            input.showWeightedSum(courses, studentsMarks);
        elif (option == "9"):
            input.sortAvg(students);

menu()