class Dog:

    kind = 'canine'
    count = 0 

    def __init__(self,name):

        self.name = name 
        Dog.count  += 1


d = Dog("Fido")
e = Dog("Buddy")
d.kind 

e.kind
d.name 
e.name
e.count
d.count 


print(e.count)