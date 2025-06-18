class A:
    def myname(self):
        print("I am a class A")
class B(A):
    def myname(self):
        print("I am in class B")
class C(A):
    def myname(self):
        print("I am in class C")

#classes ordering
class D(C,B):
    pass
d=D()
print(D.__mro__)
print(D.mro())