a,b,c,d = [int(i) for i in input().split()]

misha1 = (3*a)/10
misha2 = a - (a/250)*c

misha = max([misha1,misha2])

vasya1 = (3*b)/10
vasya2 = b - (b/250)*d

vasya = max([vasya1,vasya2])

m = max([vasya, misha])
if(misha == vasya):
    print("Tie")
elif misha>vasya:
    print("Misha")
else:
    print("Vasya")