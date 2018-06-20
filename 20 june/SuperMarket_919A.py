
n,m = [int(i) for i in input().split()]

minimum = 1000000

for i in range(n):
    a,b =  [int(i) for i in input().split()]
    price = (a/b)*m;
    minimum = min([minimum,price])

print(minimum)