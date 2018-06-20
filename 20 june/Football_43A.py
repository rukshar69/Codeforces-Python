
n = int(input())

a = 0
b = 0
s_list = []
for i in range(n):
    s = input()
    s_list.append(s)

unique_team = set(s_list)
unique_team = list(unique_team)
#print(unique_team)
for s in s_list:
    if s==unique_team[0]:
        a += 1
    else :
        b+=1

if(a>b):
    print(unique_team[0])
else:
    print(unique_team[1])