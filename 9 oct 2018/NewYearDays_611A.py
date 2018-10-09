

x = [i for i in input().split()]

if x[2] == 'month':
    temp = int(x[0])
    if(temp <=29):
        print("12")
    elif temp == 30:
        print("11")
    else:
        print("7")
else:
    temp = int(x[0])
    if(temp ==5 or temp == 6):
        print("53")
    else:
        print("52")