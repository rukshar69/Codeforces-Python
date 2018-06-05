n,m = [int(i) for i in input().split()]

x = [int(i) for i in input().split()]
turns = []
for a in x:
    if a%m == 0:
        turns.append(int(a/m))
    else:
        turns.append(int(a/m)+1)

max_turns = max(turns)
last_index = len(turns) - turns[::-1].index(max_turns) - 1
print(last_index+1)