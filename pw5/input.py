import math

# Add Information
def InputinfoStudent(students):
    id = input("Enter Id: ")
    name = input("Enter Name: ")
    dob = input("Enter dob: ")
    student = Student.Student(id, name, dob)
    students.append(student)

        f = open('Students.txt','a')
        f.write("StudentID: " + id + "\n" + "StudentName: " + name + "\n" + "StudentDoB: " + DoB)
        f.close()

# Add Course Info
def InputinfoCourse(courses):
    id = input("Enter Id: ")
    name = input("Enter name: ")
    credit = input("Enter credit: ")
    course = Course.Course(id, name, credit)
    courses.append(course)

    f = open('Courses.txt', 'a')
    f.write("CourseID: " + id + "\n" + "CourseName: " + name + "\n" + "Course_credit: " + str(credit))
    f.close()

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

    f = open('Marks.txt', 'a')
    f.write("CourseID: " + id + "\n" + "StudentID: " + id + "\n" + "Mark_detail: " + str(mark))
    f.close()
