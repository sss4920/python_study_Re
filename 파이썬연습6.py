"""
if 20kg 넘어가면 수수료 20000
20kg 미만이면 수수료 x
짐의 개수도 묻는다 먄약 짐의 개수가 2개이상이면 3만원을 더 받는다고 하자 하나라도 짐의 무게가 20키로를 초과하면 2만원을 내야한다
"""
many = int(input("짐의 개수는?"))
weight = int(input("짐의 무게는 얼마입니까?"))
pay = 0
if many >= 2:
     print("짐의 개수가 2개 이상이면 3만원을 더 내야합니다.")
     pay += 30000
    for i in many:
         if weight > 20:
             print("무거운 짐은 20000원을 내야합니다.")
             pay += 20000
else:
    if weight > 20:
        print("무거운 짐은 20000원을 내야합니다.")
        pay += 20000
    print("수수료 x")
    print("감사합니다.")
