Mark = []
Mark_GPA = []

class Marks:
    def __init__(self, Student, Courses, Marks):
        self.student = Student
        self.course = Courses
        self.mark = Marks

    def getStudent(self):
        return self.student

    def getCourse(self):
        return self.course
              + self.course.getName() + " " + str(self.mark))
