n,x = [int(i) for i in input().split()]

a = [int(i) for i in input().split()]

s = sum(a)
s = abs(s)

ans = int(s/x)
if s%x != 0: ans +=1

print(ans)