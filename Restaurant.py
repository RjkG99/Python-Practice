class FoodItem:
    def __init__(self,id1,name,category,price):
        self.item_id = id1
        self.item_name = name
        self.item_category = category
        self.item_price = price
    def provideDiscount(self,number):
            self.item_price = self.item_price - ((self.item_price *number)/100)
class Restaurant:
    def __init__(self,name,flist):
        self.restaurant_name = name 
        self.fooditem_list = flist
    def retrieveUpdatedPrice(self,itemid,percent):
        for f in self.fooditem_list:
            if f.item_id == itemid:
                f.provideDiscount(percent)
                return f


if __name__ =="__main__":
    flist =[]
    n = int(input())
    for i in range(n):
        id1 = int(input())
        name = input()
        category = input()
        price = int(input())
        flist.append(FoodItem(id1,name,category,price))
    itemid = int(input())
    percent = int(input())
    res = Restaurant("TCS",flist)
    ans = res.retrieveUpdatedPrice(itemid,percent)
    if ans==None:
        print("No Food item exists which matches the search criteria")
    else:
        print(ans.item_name,end=' ')
        print(ans.item_price,end=' ')