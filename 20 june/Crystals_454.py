n = int(input())

#UPPER HALF
diamond = 1
star = int(n/2)

limit = int(n/2)+1
for i in range(limit):

    diamonds = "D"*diamond
    starts = "*"*star
    star-=1
    diamond+=2
    string = starts+diamonds+starts
    print(string)

#lower half
limit -=1
diamond = n-2
star =1
for i in range(limit):
    diamonds = "D"*diamond
    starts = "*"*star
    string = starts+diamonds+starts
    print(string)
    star+=1
    diamond-=2
