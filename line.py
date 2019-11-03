def slope(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)

def y_intercept(l1,x1,y1):
    inter = (-x1*l1)+y1
    return inter

def x_intercept(l1,x1,y1):
    inter = (-y1/l1)+x1
    return inter
x1,y1,x2,y2 = map(int,input().split())
print("기울기:",slope(x1,y1,x2,y2))
print("y절편:",y_intercept(slope(x1,y1,x2,y2),x1,y1))
print("x절편:",x_intercept(slope(x1,y1,x2,y2),x1,y1))
