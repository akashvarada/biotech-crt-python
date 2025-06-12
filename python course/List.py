Size=int(input("Enter the Size of List: "))
List=[]
Unique_List=[]
for i in range(Size):
    Temp=int(input(f"Enter the integer Value at {i} Index position: "))
    List.append(Temp)
print(f"User entered List: {List}")
for i in List:
    if i not in Unique_List:
        Unique_List.append(i)
print(f"Unique_List : {Unique_List}")