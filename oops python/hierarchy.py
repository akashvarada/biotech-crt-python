class grandfather():
    def show(self):
        print("this is grandfather class")

class father(grandfather):
    def show1(self):
        print("this is father class")

class son(father):
    def show2(self):
        print("this is son class")

s1=son()
s1.show()
s1.show1()
s1.show2()