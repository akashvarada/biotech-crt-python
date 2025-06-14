def multiplication(n):
    print(f"Multiplication table of  {n}")
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
multiplication(n=(int(input("Enter the number : "))))
