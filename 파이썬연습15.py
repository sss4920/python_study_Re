"""
문제: 좌표를 입력받아서 좌표가 속하는 사분면을 화면에 출력하는 프로그램을 작성하라. x축, y축, 원점에 있는 경우도 있다.
작성자: 김수현
작성일:2019.09.17
입력 예)
x좌표: 3
y좌표: 5
결과 예)
좌표(3,5)는 1사분면에 있습니다.
"""
x = int(input("x좌표:"))
y = int(input("y좌표:"))
if x == 0:
    if y == 0:
        print("좌표(0,0)은 원점에 있습니다.")
    else:
        print("좌표(0,%d)는 y축에 있습니다."%y)
if x>0:
    if y < 0:
        print("좌표(%d,%d)은 4사분면에 있습니다."%(x,y))
    elif y==0:
        print("좌표(%d,0)는 x축에 있습니다."%x)
    else:
        print("좌표(%d,%d)은 1사분면에 있습니다."%(x,y))
if x<0:
    if y < 0:
        print("좌표(%d,%d)은 2사분면에 있습니다."%(x,y))
    elif y==0:
        print("좌표(%d,0)는 x축에 있습니다."%x)
    else:
        print("좌표(%d,%d)은 4사분면에 있습니다."%(x,y))
