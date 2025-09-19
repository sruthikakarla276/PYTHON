'''a=[[" " for i in range(10)] for i in range (10)]
for i in range(10):
   for j in range(10):
       if(j==0 or j==9):
           a[i][j]="*"
       elif(i==j and i<5):
            a[i][j]="*"
       elif(i+j==8 and i<5):
           a[i][j]="*"

           
for i in range(10):
    for j in range(10):
       print(a[i][j],end=" ")
    print()'''





b=int(input("enter any number: "))
a=[["A" for i in range(a+2)] [for i in range (a+2)]]
for i in range(b+2):
    for j in range(b+2):
        if (i==0 or i ==b+1 or j==0 
        elif(i%2!=0):
           a[i][j]="*"
       elif(i+j==8 and i<5):
           a[i][j]="$"
        
for i in range(b+2):
    for j in range(b+2):
        print(a[i][j],end=" ")
    
    for j in range(star-1):
            print("",end=" ")
            count=count+1
            print()
    
    
