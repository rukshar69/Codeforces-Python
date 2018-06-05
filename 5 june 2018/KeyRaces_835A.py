

x = [int(i) for i in input().split()]

s = x[0]
v1 = x[1]
v2 = x[2]
t1 = x[3]
t2 = x[4]
boy1 = s*v1 + t1*2
boy2 = s*v2 + t2*2

if boy1 > boy2:
    print("Second")
elif boy1 < boy2:
    print("First")
else :
    print("Friendship")