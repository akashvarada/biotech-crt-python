Size=int(input("Enter the size of the toys list: "))
List=[]
Unique_List=[]
for i in range(Size):
    Temp=(input(f"Enter the Toys name : "))
    List.append(Temp)
print(f"The initial List is {i}: {List}")
for i in List:
    if i not in Unique_List:
     Unique_List.append(i)
print(f"Unique_List : {Unique_List}")