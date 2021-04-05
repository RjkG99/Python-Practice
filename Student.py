class Student:
    def __init__(self,rn,name):
        self.name = name
        self.rollno = rn
    def printName(self):
        print("Name is:",self.name)

s1 = Student(123,"Rajkumar Govil")
s2 = Student(256,"ABC XYZ")
s1.printName()
s2.printName()




