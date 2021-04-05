class Table:
    def __init__(self,table,name,status):
        self.tableNo = table
        self.waiterName = name
        self.status = status
def findWaiterWiseTotalNoOfTables(tlist):
    d = {}
    for i in tlist:
        d[i.waiterName] = 0
    for i in tlist:
        d[i.waiterName] += 1
    return d 
def findWaiterNameByTableNo(tlist,tableno):
    for i in tlist:
        if i.tableNo ==tableno:
            return i.waiterName
    return "No Table Found"

if __name__ =="__main__":
    tlist = []
    n = int(input())
    for i in range(n):
        tableno  = int(input())
        waitername = input()
        status = input()
        tlist.append(Table(tableno,waitername,status))
    num = int(input())

    ans = findWaiterWiseTotalNoOfTables(tlist)
    for i in ans:
        print(i+"-"+str(ans[i]))
    print(findWaiterNameByTableNo(tlist,num))
    