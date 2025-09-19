a=int(input("enter input 1: "))
b=int(input("enter input 2: "))
c=int(input("enter input 3: "))

a1=[int(i) for i in str(a)]
b1=[int(i) for i in str(b)]
c1=[int(i) for i in str(c)]

largest=max(a1)+max(b1)+max(c1)
smallest=min(a1)+min(b1)+min(c1)
key=largest- smallest
print("the key is ",key)
