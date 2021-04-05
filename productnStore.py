class product:
    def __init__(self,pn,pt,up,qoh):
        self.pn=pn
        self.pt=pt
        self.up=up
        self.qoh=qoh

class store:
    def __init__(self,productlist):
        self.productlist=productlist
        
    def purchaseproduct(self,name,quantity):
        for i in self.productlist:
            if name==i.pn:
                if i.qoh==0:
                    print('Product not available')
                if i.qoh>quantity:
                    i.qoh=i.qoh-quantity
                    bill=i.up *quantity
                    print(bill)
                if i.qoh<quantity:
                    a=i.qoh
                    i.qoh=0
                    bill=i.up*a
                    print(bill)
if __name__ == '__main__':
    productlist=[]
    n=int(input())
    for i in range(n):
        pn=input()
        pt=input()
        up=int(input())
        qoh=int(input())
        productlist.append(product(pn, pt, up, qoh))
    obj=store(productlist)  
    name=input()
    quantity=int(input())
    obj.purchaseproduct(name, quantity)
    for i in productlist:
        print(i.pn,end=' ')
        print(i.qoh)
