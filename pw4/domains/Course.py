Courses = []
CoursesId = []
Credit = []

class Course:
    def __init__(self, Cid,Cname,Ccredit):
        self.Cid = Cid
        self.Cname = Cname
        self.Ccredit = Ccredit

    def describe(self):
        print("Id: " + self.Cid + " Course name: " + self.Cname + " credit: " + self.Ccredit)

    def getName(self):
        return self.Cname
