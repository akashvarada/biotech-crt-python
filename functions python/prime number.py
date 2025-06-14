def prime_number(Num):
    if(Num>1):
        Count=0
        for i in range(1,Num+1):
            if(Num%i==0):
                Count+=1
        if(Count==2):
            print(f"{Num} is Prime")
        else:
            print(f"{Num} is not prime")
    else:
        print(f"{Num} is not prime")
prime_number(17)
prime_number(18)
prime_number(7)
prime_number(0)
