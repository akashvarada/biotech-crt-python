class Father:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name)

class Son(Father):
    def __init__(self,name):
        self.name=name
    def show1(self):
        print(self.name)

x=Father('Nagarjuna')
x.show()
y=Son("akhil")
y.show1()
y.show() 

class base:
    def __init__(self):
        self._a=32
        print(self._a)

class derived(base):
    def __init__(self):
        base.__init__(self)
        print(self._a+2)

x=base()