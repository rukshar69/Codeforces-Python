

s = input()

flag = True
#if any(x in str for x in a):
a = ['2','3','5','6','7','8','9','0']
if s[0] != '1':
    flag = False
if '444' in s:
    flag = False
if any(x in s for x in a):
    flag = False

if flag == True:
    print("YES")
else:
    print("NO")