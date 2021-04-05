class Passenger:
    def __init__(self,name,ticket):
        self.name = name 
        self.ticket = ticket


class Price:
    def __init__(self,plist):
        self.plist = plist
    def getDetails(self):
	
        for i in self.plist:
            i.ticket = i.ticket *50 
            print(i.name)
            print(i.ticket)


if __name__ == "__main__":
    n = int(input())
    plist = []
    for i in range(n):
        name = input()
        ticket = int(input())
        plist.append(Passenger(name,ticket))
    price = Price(plist)
    price.getDetails()
    
    
        