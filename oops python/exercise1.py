class student:
    def __init__(self,name,rno,mat,phy,chem):
        self.name=name
        self.rno=rno
        self.mat=mat
        self.phy=phy
        self.chem=chem

    def calculation(self):
        if(self.mat>=40 and self.phy>=40 and self.chem>=40):
            total=self.mat+self.phy+self.chem
            avg=total/3
            print(total)
            if(self.mat>75 and self.phy>75) or (self.phy>75 and self.chem>75) or (self.mat>75 and self.chem>75):
                print("admission is confirmed")
            else:
                print("admission is not confirmed")
        else:
            print("fail")
s1=student("kiran",150,76,80,45)
s1.calculation()