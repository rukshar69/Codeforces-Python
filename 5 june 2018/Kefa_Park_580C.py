n,m = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]


List_ = []
for i in range(n):
    List_.append([])
for i in range(n-1):
    x,y = [int(i) for i in input().split()]
    x -=1
    y -=1
    List_[y].append(x)
    List_[x].append(y)

p = 0
def traverse_graph(vertice, parent, k):
    if(k>m): return
    ok = 1
    temp_list = List_[vertice]
    length = len(temp_list)
    for i in range(length):
        if temp_list[i] != parent:
            ok = 0
            traverse_graph(temp_list[i],vertice,k*c[temp_list[i]]+c[temp_list[i]])
    global p
    p += ok

print(p)