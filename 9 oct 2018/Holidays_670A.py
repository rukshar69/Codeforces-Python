n = int(input())

if n<6:
    print("0 2")
elif n == 6:
    print("1 2")
elif n==7:
    print("2 2")
else:
    weekday = 1
    dayoff = 0
    for i in range(1,n+1):
        if weekday%6 == 0 or weekday%7 ==0:
            dayoff+=1
        weekday += 1
        if weekday>7:
            weekday =1
    print(dayoff, end="", flush=True)

    weekday = 6
    dayoff = 0
    for i in range(1,n+1):
        #print("weekday ",weekday)
        if weekday%6 == 0 or weekday%7 ==0:
            dayoff+=1
        weekday += 1
        if weekday>7:
            weekday =1
    print(" ",dayoff)