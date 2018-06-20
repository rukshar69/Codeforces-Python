n = int(input())

flag = False
for i in range(n):
    x = [i for i in input().split()]
    if int(x[1])>=2400 and int(x[2])>int(x[1]):
        flag = True

if flag:
    print("YES")
else : print("NO")

