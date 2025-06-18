class person:
    def __init__(self,name,age): #instance variables
        self.name=name
        self.age=age

p1=person('Akash',21)
p2=person('rk',55)
print(p1.name,p1.age,sep=" - ")
print(p2.name,p2.age,sep=" - ")

class person:
    def __init__(se,name,age): #instance variables
        se.name=name
        se.age=age

    def printing(self):
        print(self.name,self.age)
p1=person('Akash',21)
p2=person('rk',55)
p1.printing()
p2.printing()