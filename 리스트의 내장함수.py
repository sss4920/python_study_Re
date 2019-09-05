# 리스트 (내장함수)

li = [3, 1, 4,'움칫',4,5,1]

# 인덱싱 슬라이싱

#print(li[0:2])

# 리스트의 길이를 구해주는 함수 : len(변수)

#print(len(li))

# 리스트 원소 오름차순 정렬해주는 함수 : 변수, sort()
print(li)

li.sort() # 리스트로 반환 안하기 때문에 print(li.sort())하면 아무것도 안나옴

print(li)
# 리스트 내의 특정 원소 인덱스 반환해주는 함수 : .index()

print(li.index('움칫'))