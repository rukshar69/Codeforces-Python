

x = [int(i) for i in input().split()]
a = x[0]
b = x[1]
a_p = 0
b_p= 0
draw = 0

for i in range(1,7):
    diffA = abs(a-i)
    diffB = abs(b-i)
    if diffA<diffB:
        a_p += 1
    elif diffB<diffA:
        b_p += 1
    else:
        draw += 1

print(a_p,draw,b_p,)
