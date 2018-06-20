na, nb =  [int(i) for i in input().split()]
k,m  = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
count = 0
for x in a:
    tempCount = 0
    for y in b:
        if x<y:
            tempCount +=1
    if tempCount >=m:
        count+=1
if count>=k:
    print("YES")
else:print("NO")