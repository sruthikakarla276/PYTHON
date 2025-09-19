def find(x,y,z):
    ht=0
    time=0
    step=1
    while (ht<x):
        if (step%2!=0):
            ht=ht+y
            time+=1
            step=step+1
        else:
            ht=ht-z
            time+=1
            step=step+1
    print("the total min is",time)
find(21,5,3)