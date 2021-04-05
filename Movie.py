class Movie:
    def __init__(self,movie_id,movie_name,ticket_cost):
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.ticket_cost = ticket_cost
        self.category = "default"
    def Price_category(self):
        if self.ticket_cost > 0 and self.ticket_cost < 150:
            self.category = "Genral"
        elif self.ticket_cost >=150 and self.ticket_cost < 250:
            self.category = "Silver"
        elif self.ticket_cost >=250 and self.ticket_cost < 350:
            self.category = "Gold"
        else:
            self.category = "Platinum"


class Movie_Ticket:
    def __init__(self,customer_name,movie_name,viwerCount,totalTicketCost):
        self.customer_name = customer_name
        self.movie_name = movie_name
        self.viwerCount = viwerCount
        self.totalTicketCost = totalTicketCost 


def getCategoryWiseCount(mlist):
    dict = {}
    for m in mlist:
        m.Price_category()
    for m in mlist:
        cost = m.category
        if cost not in dict.keys():
            dict[cost] = 1
        else:
            dict[cost] = dict[cost]+1
    return dict 


def  bookMovieTicket(mlist,cn,mn,count):
    for m in mlist:
        val = m.movie_name.lower() == mn.lower()
        if (val):
            total_ticket_cost = m.ticket_cost * count
            return total_ticket_cost


if __name__ =="__main__":
    mlist = []
    N = int(input())
    for i in range(N):
        a = int(input())
        b = input()
        c = int(input())
        mlist.append(Movie(a,b,c))
    cn = input()
    mn = input()
    count = int(input())
    dict = getCategoryWiseCount(mlist)
    b = bookMovieTicket(mlist,cn,mn,count)
    print("Category wise ticket count:") 
    for obj in dict:
        print(obj,dict[obj])
    print(cn,b)