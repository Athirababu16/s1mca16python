result=[]
start=int(input("enter the starting range(four-digital number):"))
end=int(input("enter the ending range(four-digital number):"))
if start<1000 or end>9999 or start>end:
    print("invalidrange.please enter a valid four-digit range,")
else:
    for num in range(start,end+1):
        if num%2==0:
            root=int(num**0.5)
        if root*root==num:
            result.append(num)
    print("four-digit even perfect square number in the given range:")
    print(result)
