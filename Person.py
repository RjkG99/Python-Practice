class Person:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight

class Society:
    def __init__(self,plist):
        self.plist = plist
    def findAverageHeight(self):
        avgh = 0 
        for p in self.plist:
            avgh += p.height
        avgh =(avgh/len(self.plist))
        return avgh
    def findTallerThanAgeragePerson(self):
        result = []
        avgh = self.findAverageHeight()
        for p in self.plist:
            if p.height>avgh:
                result.append(p.name)
        return result 


if __name__ =="__main__":
    plist = []
    n = int(input())
    for i in range(n):
        name = input()
        height = int(input())
        weight = int(input())
        plist.append(Person(name,height,weight))
    society = Society(plist)
    print("The Average height is",society.findAverageHeight())
    result = society.findTallerThanAgeragePerson()
    for i in result:
        print(i)