a=int(input("enter lower range"))
b=int(input("enter higher range"))
for i in range(a,b):
      count=0
      for j in range(2,i):
          if (i%j==0):
              count=count+1
      if (count==0):
          print(i,end=" ")
