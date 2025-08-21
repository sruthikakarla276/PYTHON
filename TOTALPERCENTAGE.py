a=["Harsha","Siri","Preethi","Mahi"]
mark=[[76,45,34,78],[54,56,76,89],[34,98,87,90],[89,87,86,84]]
per=[]
for i in mark:
    d=sum(i)//4
    per.append(d)
for i in range(4):
    print("{}. {} : {}%".format(i+1,a[i],per[i]))
