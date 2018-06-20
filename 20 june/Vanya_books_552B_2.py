n = int(input())

count = 0
x=n
while n!=0:
    count+=1
    n/=10

sum = 0
for i in range(count):
    sum = (sum*10)+1

ans = count*(x+1) - sum
print(ans)