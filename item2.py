class Item:
	def _init_(self,itemName,itemType,unitPrice):
		self.itemName=itemName
		self.itemType=itemType
		self.unitPrice=unitPrice
class Store:
	def _init_(self,itemInventory):
		self.itemInventory=itemInventory
	def buyItem(self,item,quantity):
		for items,quantityInHand in itemInventory.items():
			if(items.itemName.lower()==item.lower() and quantity==0):
				return None
			if(items.itemName.lower()==item.lower() and quantity>quantityInHand):
				itemInventory[items]=0
				return items.unitPrice*quantityInHand
			if(items.itemName.lower()==item.lower() and quantity<=quantityInHand):
				itemInventory[items]=quantityInHand-quantity
				return items.unitPrice*quantity
		return None
n=int(input())
itemInventory={}
for i in range(n):
	itemName=input()
	itemType=input()
	unitPrice=int(input())
	quantityInHand=int(input())
	itemInventory[Item(itemName,itemType,unitPrice)]=quantityInHand
store1=Store(itemInventory)
order={}
num=int(input())
for i in range(num):
	itemName=input()
	quantity=int(input())
	order[itemName]=quantity
for itemName,quantity in order.items():
	billAmount=store1.buyItem(itemName,quantity)
	if(billAmount==None):
		print(itemName,"is not available")
	else:
		print("Bill of the item ",itemName,"=",billAmount)
print("Stock in Hand:")
for item,quantityInHand in store1.itemInventory.items():
	print(item.itemName,quantityInHand,sep=" ")