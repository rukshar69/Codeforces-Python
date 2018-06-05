n,k = [int(i) for i in input().split()]

for i in range(n):
    f,t = [int(i) for i in input().split()]
    if i == 0:
        if t<=k:
            max_joy = f
        else:
            max_joy = f - (t-k)
    else:
        if t<=k:
            temp_joy = f
        else:
            temp_joy = f - (t-k)
        max_joy = max([max_joy,temp_joy])

print( max_joy)