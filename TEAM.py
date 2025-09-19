import random
no=int(input("enter the no of teams"))
team=[]
for i in range(no):
    d=input("enter the team names")
    team.append(d)
meet=input("enter the no.meetings")
matches=[]
for i in range(no-1):
    for j in range(i+1,no):
        for k in range(no):
            matches.append([team[i],team[j]])
random.shuffle(matches)
for i in range (len(matches)):
    print("matches{}:{} VS {}".format(i+1,matches[i][0],matches[i][1]))
