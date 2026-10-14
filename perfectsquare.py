result=[]
start=int(input("Enter te starting range(Four-Digit Number):"))
end=int(input("Enter te ending range(Four-Digit Number):"))
if start<1000 or end>9999 or start>end:
    print("Invalid range .please enter  valid four digit range.")
else:
    for num in range(start,end+1):
        if num%2==0:
            root=int(num**0.5)
        if root*root == num:
            result.append(num)
print("for digit even perfect square number in the given range.")
print(result)
        
        
