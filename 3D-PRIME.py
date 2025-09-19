a=int(input("enter the number of 3-digits"))
for a in range(100,1000):
    for i in range(a):
      count=0
      for j in range(2,i):
          if (i%j==0):
              count=count+1
      if (count==0):
          sum=0
          for k in string(a):
              sum=sum+k
    else:
        print("the digits of a number is not prime")
            
              
    
    
    
