import input as inp
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
            inp.AddinforStudent(students)
        elif (option == "2"):
            inp.AddinforCourse(courses)
        elif (option == "3"):
            inp.inputMark(courses, students, studentsMarks)
        elif (option == "4"):
            inp.ShowlistStudents(students)
        elif (option == "5"):
            inp.ShowlistCourses(courses)
        elif (option == "6"):
            inp.ShowMarks(studentsMarks)
        elif (option == "7"):
            inp.showAvarage(students)
        elif (option == "8"):
            inp.showWeightedSum(courses, studentsMarks);
        elif (option == "9"):
            inp.sortAvg(students);

menu()