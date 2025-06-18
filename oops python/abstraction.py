from abc import ABC,abstractmethod
class car(ABC):
    @abstractmethod
    def mileage(self):
        pass
class tesla(car):
    def mileage(self):
        print("mileage is 20kmph")

class suzuka(car):
    def mileage(self):
        print("mileage is 12kmph")

t1=tesla()
t1.mileage()
s1=suzuka()
s1.mileage()