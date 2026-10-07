num_list=[]
n=int(input("enter the number of values to list:"))
print("enter the elements to list:")
for i in range(n):
    val=int(input())
    num_list.append(val)
total=0
for item in num_list:
    total=total+item
print("the sum of items in the list is:",total)






















