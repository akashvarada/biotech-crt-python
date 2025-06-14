def Hello():
    print("Hello World")
Hello()
print(Hello())

def Display(a):
    print("a :",a())
def demo():
    print("Hey....!I'm a demo function...!")
Display(demo)

def display():
            def show():
                  return "show function"
            print("Disp Function")
            return show 
r_sh = display()
print(r_sh())

def Print(a,b):
      print(f"a :",a)
      print(f"b :",b)
#print(a,b) #Parameter
Print(10,20) #Argument