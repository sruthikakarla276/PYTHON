
a=["Harsha","Siri","Preethi","Mahi"]
mark=[[76,45,34,78],[54,56,76,89],[34,98,87,90],[89,87,86,84]]
per=[]
for i in mark:
    d=sum(i)//4
    per.append(d)
for i in range(4):
    print("{}. {} : {}%".format(i+1,a[i],per[i]))


'''
student=["ANU","ANIL","BALA","RAVI","RAJU","JACK"]
cgpa=[59,66,47,88,78,69]
arrear=[0,1,2,1,0,0]
for i in range(6):
    if arrear[i]==0 and cgpa[i]>60:
        print (student[i])



import random
l=[]
while len(l)<5:
    d=random.randint(1,10)
    if d not in l:
        l.append(d)
print(l)




for i in range(1,11):
    for j in range(1,11):
        print(i*j,end="  ")
    print()


for i in range(1,10):
    for j in range(i):
        print("*",end="  ")
    print()'''




