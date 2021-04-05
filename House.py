class HouseForSale:
    def __init__(self,hnum,htype,sp,a,i):
        self.houseNumber=hnum
        self.houseType=htype
        self.salePrice=sp
        self.areainSqft=a
        self.Furnished=i
        
    def calculateNewPrice(self,r):
        self.salePrice=self.areainSqft*r
        if(self.Furnished=="SEMI FURNISHED"):
            self.salePrice=self.salePrice*1.10
        elif(self.Furnished=="FULLY FURNISHED"):
            self.salePrice=self.salePrice*1.20
        return(self.salePrice)
    
class Realtor:
    def __init__(self,rt,nr,hlist):
        self.realtorld=rt
        self.newRate=nr
        self.listOfHouseForSale=hlist
        
    def getAvailableHouses(self,sale_price,house_type):
        hlist1=[]
        pv=self.listOfHouseForSale
        for x in pv:
            new_price=x.calculateNewPrice(self.newRate)
            if(new_price<=sale_price and x.houseType==house_type):
                hlist1.append(x)    
        return hlist1
    
if __name__=="__main__":
    no=int(input())
    hlist=[]
    while(no>0):
        hn=int(input())
        ht=input()
        sp=float(input())
        ars=int(input())
        iff=input()
        no-=1
        pv=HouseForSale(hn,ht,sp,ars,iff)
        hlist.append(pv)
        
    nr=int(input())
    rea=Realtor(123,nr,hlist)
    h_type=input()
    s_price=float(input())
    result=rea.getAvailableHouses(s_price,h_type)
    if(len(result)==0):
        print("Preferred House Not Available")
    else:
        for x in result:
            print(x.houseNumber,x.houseType,x.areainSqft,x.salePrice)