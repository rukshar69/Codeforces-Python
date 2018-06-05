
x = [int(i) for i in input().split()]
n = x[0]
d = x[1]

consecutive = 0
max_consecutive = -1
for i in range(d):
    s = input()
    if '0' in s:
        consecutive+=1

    elif '0' not in s:
        consecutive = 0
    max_consecutive = max(max_consecutive, consecutive)

print(max_consecutive)
