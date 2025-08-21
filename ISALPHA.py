a=input("enter any string")
res=""
for i in a:
    if (i.isalpha()):
        res=res+i
res1=res.capitalize()
print(res1)
