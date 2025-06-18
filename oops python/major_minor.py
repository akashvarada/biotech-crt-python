class person:
    def __init__(se,name,age): #instance variables
        se.name=name
        se.age=age

    def printing(self):
        print(self.name,self.age)
    
    def decide(self):
        if(self.age>=18):
                print("major")
        else:
                print("minor")
    def uppercaseconversion(self):
        print(self.name.upper())
p1=person('Akash',21)
p2=person('rk',55)
p1.printing()
p2.printing()
p1.decide()
p2.decide()
p1.uppercaseconversion()
p2.uppercaseconversion()

