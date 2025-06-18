class shop:
    def __init__(self,name,itemscount):
        self.name=name
        self.itemscount=itemscount
    def calculation(self):
        x=self.itemscount
        tp=0
        for i in range(x): 
            p=int(input())
            tp+=p
        return tp 
name=input()
itemscount=int(input())
c1=shop(name,itemscount)
tp=c1.calculation()
if(tp>=200):
    print(tp-tp*0.2)
else:
    print(tp)