n = input()
len_n = len(n)

flag = False
result = ""
for i in range(len_n):
    a = n[i]
    if(int(a)%8 == 0):
        flag = True
        result = a
        break
    for j in range(i+1, len_n):
        b = a+n[j]
        if(int(b)%8 == 0):
            flag = True
            result = b
            break
        for k in range(j+1, len_n):
            c = b+n[k]
            if(int(c)%8 == 0):
                flag = True
                result = c
                break

if(flag == True):
    print("YES")
    print(result)
else:
    print("NO")