sample_prefix=int(input("Enter the Lab sample prefix : "))
sample_format=""
num=int(input("Enter the no.of ID's you have to generate: "))
list=[]
for i in range(0,num):
    sample_format=(f"LAB2025-0{sample_prefix+1}")
    list.append(sample_format)
    sample_prefix+=1
print(list)