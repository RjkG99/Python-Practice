class Container:
    def __init__(self,id1,length,breadth,height,pricePerSqrFt):

        self.id1 = id1
        self.length = length
        self.breadth  = breadth 
        self.height = height 
        self.pricePerSqFt = pricePerSqrFt

    def findVolume(self):
        return self.length * self.breadth * self.height
    
class PackagingCompany:

    def __init__(self,containerlist):
        self.containerlist = containerlist
    
    def findContainerCost(self,inid):

        for i in self.containerlist:
            if i.id1==inid:
                k = i.findVolume()
                cost = k *i.pricePerSqFt
                return cost
        return None


    def findLargestContainer(self):
        out={}
        for i in self.containerList:
            k=i.findVolume()
            out[k]=i.id
        out=sorted(out.items(),reverse=True)
        return out

if __name__ == '__main__':

    count=int(input())
    clist=[ ]
    for i in range(count):
        iid=int(input())
        l=int(input())
        b=int(input())
        h=int(input())
        p=int(input())
        c1=Container(iid,l,b,h,p)
        clist.append(c1)
    p1=PackagingCompany(clist)
    inid=int(input())
    res1=p1.findcontainercost(inid)
    res2=p1.findmaxvolume()
    if(res1==None):
        print("No container found")
    else:
        print(res1)
    print(res2[0][1],res2[0][0])
    

