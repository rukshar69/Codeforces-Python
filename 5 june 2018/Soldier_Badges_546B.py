n = int(input())

a = [int(i) for i in input().split()]

sorted(a)
coin = 0
for i in range(1,n):
    if a[i] == a[i-1]:
        a[i] = a[i]+1
        coin += 1
    elif a[i]<a[i-1]:
       diff =  a[i-1] -a[i]
       a[i] += diff
       coin += diff
       coin +=1
       a[i] += 1

print(coin)