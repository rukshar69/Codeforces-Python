import  math
r, x, y, x_, y_ = [int(i) for i in input().split()]

dist = math.sqrt( (x - x_)**2 + (y - y_)**2 )

result = math.ceil(dist/(2*r))

print(result)