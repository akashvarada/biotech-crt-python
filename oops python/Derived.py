class Calculation1:
    def Summation(self,a,b):
        return a+b;
class Calculation2:
    def Multiplication(self,a,b):
        return a*b;
class Derived(Calculation1,Calculation2):
    def Divide(self,a,b):
        return a/b;
d=Derived()
print(issubclass(Derived,Calculation1))
print(issubclass(Derived,Calculation2))
print(issubclass(Calculation1,Calculation2))

class Calculation1:
    def Summation(self,a,b):
        return a+b;
class Calculation2:
    def Multiplication(self,a,b):
        return a*b;
class Derived(Calculation1,Calculation2):
    def Divide(self,a,b):
        return a/b;
d=Derived()
print(isinstance(d,Derived))
print(isinstance(d,Calculation1))
print(isinstance(d,Calculation2))
