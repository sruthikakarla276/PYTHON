def total_time(x,y,z):
    h=0
    m=0
    while h<x:
        m+=1
        h+=y
        if h>=x:
            break
        m+=1
        h-=z
    return m
x=int(input("enter input 1: "))
y=int(input("enter input 2: "))
z=int(input("enter input 3: "))
print("time:",total_time(x,y,z), "m")
