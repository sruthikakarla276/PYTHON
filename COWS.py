a=int(input("enter no.of legs"))
b=int(input("enter no.of heads"))
flag=False
for cow in range(b+1):
    hen=b-cow
    if cow*4 + hen*2 == a :
        flag=True
        print("the no of cows",cow)
        print("the no of hens",hen)
if(flag==False):
    print("No solution")