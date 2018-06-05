n = int(input())

x = [int(i) for i in input().split()]


sereja_sum = 0
dima_sum = 0
turn = 0

left = 0
right = n-1

while left <right+1:

    if x[left] > x[right]:
        max = x[left]
        left += 1
    else :
        max = x[right]
        right -=1

    if turn == 0:
        sereja_sum += max
        turn = 1
    else:
        dima_sum += max
        turn = 0



print(sereja_sum,dima_sum)