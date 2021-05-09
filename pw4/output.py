import numpy

def ShowlistCourses(courses):
    print("Show course List:")
    for c in courses:
        c.describe()


def ShowlistStudents(students):
    print("Show student List:")
    for s in students:
        s.describe()


def ShowMarks(studentMarks):
    courseName = input("Enter name of course to show marks: ")
    print("Student Marks for " + courseName)
    for studentMark in studentMarks:
        if courseName == studentMark.getCourse().getName():
            studentMark.describe()

def calculateAvg(id, studentMarks):
    marks = []
    for studentMark in studentMarks:
        if (studentMark.getStudent().getId() == id):
            marks.append(studentMark.getMark())
    return numpy.average(marks)

def showAvarage(students):
    id = input("Input student id: ")
    for s in students:
        if id == s.getId():
            print("Name: " + s.getName() + " Avg: " + str(s.getAvg()))

def sortAvg(students):
    sortedList = sorted(students, key=lambda x: x.getAvg(), reverse=True)
    for s in sortedList:
        s.describe()

def calculationWeightedSum(id, courses, studentMarks):
    sum = 0
    for c in courses:
        smark = []
        warray = []
        for studentMark in studentMarks:
            if (studentMark.getStudent().getId == id):
                smark.append(studentMark.getMark())
                warray.append(c.etc)
        weights = numpy.array(warray)
        amark = numpy.array(smark)
        sum = sum + numpy.sum(numpy.dot(amark, weights))
    return sum

def showWeightedSum(courses, studentMarks):
    id = input("Input student id: ")
    print("Weighted sum: " + str(calculationWeightedSum(id, courses, studentMarks)))