'''MENU:
    1) SQUARE
    2)RECTANGLE
    3)CIRCLE
    4)TRIANGLE
    5)EXIT
ENTER U R CHOICE:1
ENTER SIDES OF SQUARE:20
AREA OF SQ IS 400


while(1):
    print("___MENU____")
    print("1. SQUARE")
    print("2.RECTANGLE")
    print("3.CIRCLE")
    print("4.TRIANGLE")
    print("5.EXIT")
    a=int(input("ENTER YOUR CHOICE: "))
    if(a==1):
        sq()
    elif(a==2):
        l=int(input("ENTER LENGTH OF RECT: "))
        b=int(input("ENTER BREADTH OF RECT: "))
        rect(l,b)
    elif(a==3):
        x=circle()
        print("the radius of circle")
    elif(a==4):
        l=int(input("ENTER LENGTH OF TRI: "))
        b=int(input("ENTER BREADTH OF TRI: "))
        l=int(input("ENTER HEIGHT OF TRI:  "))
    elif(a==5):



    
       '''
def gcb(a,b):
    while(b!=0):
        res= a%b
        a=b
        b=res
def cop():
    cop(a,b)

    
a=int(input("enter any number"))
for i in range(5,a):
    for j in range(4,i):
        for k in range(3,j):
            if(j*j+k*k==i*i and cop(i,j) and cop(j,k) and cop(i,k)):
                print(k,j,i)








































































    
        
