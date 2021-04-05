"""7. A bookshop has many books belonging to different categories like horror, romance, non-fiction etc. 
Each book has a name, ID,price, category and the author name.
 The bookshop wants an automated system with which it can get  the price of a particular book. 
Also, the bookshop wants the system to update the price of a given category of books if needed by a given price.
 Implement the scenario using OOP in Python."""

class Book :
    def __init__(self,name,id1,price,category,author_name):
        self.name = name
        self.id1 = id1
        self.price = price
        self.category = category
        self.author_name = author_name
    
    def get_price(self):
        return self.price


    def print_book_details(self):
        print("Name",self.name,"\nid ",self.id1,"\nPrice",self.price,"\nCateogry",self.category,"\nAuthor ",self.author_name)

book1 = Book("The Love",1,225,"Romance","Shakespeare")

book1.print_book_details()
print(book1.get_price())

        