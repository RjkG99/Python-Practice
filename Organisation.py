class Employee:

    def __init__(self,name,eid,age,gender):
        self.eid = eid 
        self.name = name
        self.age = age 
        self.gender = gender


class Organisation:

    def __init__(self,name,elist):
        self.name = name 
        self.elist = elist

    def addEmployee(self,eid,name,age,gender):
        print("In addEmployee Function")
        e = Employee(eid,name,age,gender)
        print("End addEmployee Function")

    def viewEmployees(self):
        print("In View Employee Function")
        for e in self.elist:
            print(e.eid)
            print(e.ename)
            print(e.age)
            print(e.gender)
        print("End View Employee function")


    def getEmployeeCount(self):
        print("In countEmployeee  function")
        print("End countEmployee function")
        return len(self.elist)
    
    def findEmployeeAge(self,eid):
        print("IN findEmployeefunction")
        age =-1
        for e in self.elist:
            if e.eid ==eid:
                age = e.age
                break

        print("End odf find Employee funtion")

        return age

    def countEmployee(self,eid):
        count = 0
        print("IN countEmployeefunction")
        for e in self.elist:
            if e.age > age:
                count +=1

    

        print("End of count Employee funtion")

        return count


if __name__ =='__main__':

    employee = []
    o = Organisation("TCS",employee)
    n = int(input())
    for i in range(n):
        name = input()
        eid = input()
        age = int(input())
        gender = input()
        o.addEmployee(name,eid,age,gender)

    o.viewEmployees()

    print(o.getEmployeeCount())

    eid = int(input())
    print(o.findEmployeeAge(eid))

age = int(input())
print(o.countEmployee(age))





    
