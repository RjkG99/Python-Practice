class Employee:
    def __init__(self,id1,name,agenInrole):
        self.employeeId = id1
        self.employeeName = name
        self.status = 'In Service'
        self.agenInRole = agenInrole
class Organisation:
    def __init__(self,emplist):
        self.employeeList = emplist
    def updateEmployeeStatus(self,years):
        for e in self.employeeList:
            if e.agenInRole>years:
                e.status = "Retirement Due"
    def countEmployees(self):
        count = 0
        for e in self.employeeList:
            if e.status == "Retirement Due":
                count +=1
        return count 

if __name__ =="__main__":
    emplist = []
    n = int(input())
    for i in range(n):
        eid = int(input())
        ename =input()
        ageinrole = int(input())
        emplist.append(Employee(eid,ename,ageinrole))
    org = Organisation(emplist)
    year = int(input())
    org.updateEmployeeStatus(year)
    print("Conut of employee updated=",org.countEmployees())
    for i in emplist:
        print(i.employeeId,' ',i.employeeName," ",i.status)
  
         