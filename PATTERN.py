star=int(input("enter the number of star: "))
block=int(input("enter the number of blocks: "))
line=int(input("enter the number of lines: "))
for i in range(block):
    count=0
    for j in range(line-i):
        for k in range(star):
            print("*",end=" ")
            count=count+1
        print()
    print(count)
    print("______________")



