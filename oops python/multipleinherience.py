
#Multiple Inheritence
class father:
    fathername=''
    def father(self):
        print(self.fathername)
class mother:
    mothername=''
    def mother(self):
        print(self.mothername)
class son1(father,mother):
    son1name=''
    def son1information(self):
        print(self.fathername)
        print(self.mothername)
        print(self.son1name)
s1=son1()
s1.son1name="Prashu"
s1.fathername="Shiva"
s1.mothername="Pavani"
s1.son1information()

#Heirarchial
class son1(father,mother):
    son1name=''
    def son1information(self):
        print(self.fathername)
        print(self.mothername)
        print(self.son1name)
class son2(father):
    son2name=''
    def son2information(self):
        print(self.fathername)
        print(self.son2name)
s1=son1()
s1.son1name="Prashu"
s1.fathername="Shiva"
s1.mothername="Pavani"
s1.son1information()
s2=son2()
s2.fathername="Shiva"
s2.son2name="Praveen"
s2.son2information()
s1.father()