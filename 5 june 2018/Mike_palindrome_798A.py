


test = input()
#print(test)
n = len(test)
#print(n)
j = n-1
mismatch = 0
for i in range(int(n/2)):
    a = test[i]
    b = test[j]
    j -= 1
    if a != b:
        mismatch += 1
if mismatch>1:
    print("NO")
elif mismatch == 1:
    print("YES")
else:
    if n%2 == 1:
        print("YES")
    else:
        print("NO")

