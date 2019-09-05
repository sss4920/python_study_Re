import turtle
t=turtle.Pen()

while True:
    real = input("왼쪽 = left, 오른쪽=right:")
    if real == "left":
        t.left(60)
        t.forward(50)
    if real == "right":
        t.right(60)
        t.forward(50)
        
