import line

x1,y1,x2,y2 = map(int,input().split())
print("기울기:",line.slope(x1,y1,x2,y2))
print("y절편:",line.y_intercept(slope(x1,y1,x2,y2),x1,y1))
print("x절편:",line.x_intercept(slope(x1,y1,x2,y2),x1,y1))
