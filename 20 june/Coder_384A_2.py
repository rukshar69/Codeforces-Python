n = int(input())

print( (n * n + 1) / 2);

for row in range(n):
    for col in range(n):
        if (row+col)%2 == 1:
            print(".",end="", flush=True),
        else: print("C",end="", flush=True),
    print()
