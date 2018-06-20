n = int(input())

total = 0
#naive
for i in range(1,n+1):
    s = str(i)
    total += len(s)

print(total)
