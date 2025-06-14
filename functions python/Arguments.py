#Positional arguments
def pw(x,y):
    z=x**y
    print(z)
pw(5,2)

#Keyword argument
def show(name,age):
        print(name,age)
show(name="Akash varada",age=21)

#Default Arguments
def show(name,age=21):
      print(name,age)
show(name="Akash varada",age=21)

#Variable Length Arguments
def add(*num):
       z = num[0]+num[1]+num[2]
       print(z)
add(5,2,4)

#Keyword variable length
def add(**num):
      z=num['a']+num['b']+num['c']
      print(z)
add(a=5,b=2,c=4)