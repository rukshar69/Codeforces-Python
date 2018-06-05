n = int(input())
x = [int(i) for i in input().split()]

x = [0] + x

min_cos = 0
energy = 0
for i in range(n):
    a = x[i]
    b = x[i+1]
    diff = a-b
    energy += diff
    if energy<0:
        min_cos += (-energy)
        energy = 0

print(min_cos)