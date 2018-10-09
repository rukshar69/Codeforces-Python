n  = int(input())
x = [int(i) for i in input().split()]

x = [a - (1-(a%2)) for a in x]
for a in x:
    print(a,"", end="", flush=True)