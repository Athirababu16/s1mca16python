mydict1={}
print("enter elemnets of the first die:")
while True:
    key=input("enter a key (or 'q' to quit):")
    if key=='q':
        break
    value=int(input("enter a value:"))
    mydict1[key]=value
print("enter elemnets of the second die:")
mydict2={}
while True:
    key=input("enter a key (or 'q' to quit):")
    if key=='q':
        break
    value=int(input("enter a value:"))
    mydict2[key]=value
print(mydict1|mydict2)
