a = int(input())
b = int(input())
c = int(input())

total = 0
for i in range(a,0,-1):
    lemon = i
    apple = 2*i
    pear = 4*i
    if apple<=b and pear<= c:
        total = lemon+apple+pear
        break

print(total)