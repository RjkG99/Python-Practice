class Player:
    def __init__(self,name,country,age,countryfrom):
        self.playerName = name
        self.playedcountry= country
        self.playerAge = age 
        self.countryFrom = countryfrom

def countPlayers(plist,country):
    count = 0
    for i in plist:
        if i.countryFrom ==country:
            count += 1
    return count

def getPlayerPlayedForMaxCountry(plist):
    max = 0
    name = ''
    for i in plist:
        if (len(i.playedcountry)>max):
            max = len(i.playedcountry)
    for i in plist:
        if len(i.playedcountry) == max:
            name = i.playerName
    return name


if __name__ =="__main__":
    n = int(input())
    plist = []
    for i in range(n):
        name = input()
        c = int(input())
        cp = []
        for i in range(c):
            ele = input()
            cp.append(ele)
        age = int(input())
        countryFrom = input()
        plist.append(Player(name,cp,age,countryFrom))
    country = input()
    print(countPlayers(plist,country))
    print(getPlayerPlayedForMaxCountry(plist))
