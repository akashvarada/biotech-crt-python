class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=person('akash',21)
print(getattr(p1,'name'))
print(getattr(p1,'age'))
setattr(p1,'age',40)
print(getattr(p1,'age'))
print(hasattr(p1,'age'))
print(hasattr(p1,'id'))