#문자열 (내장함수)

#덧셈

str = "멋쟁이 사자처럼"

print(str[0:4])
print(len(str))

# 문자열의 길이를 알려주는 내장함수 : len(문자열 변수)

# 문자열 내에서 특정 문자의 등장 횟수 : 문자열 변수.count('특정문자')

# print(str.count('사'))

# [x:y] --> x번째 인덱스부터 y인덱스 "전까지"

# 문자열을 (특정 기준으로) 나누기 : 문자열 변수.split()

#print(str.split()) # 공백을 기준으로 나누겠다. 쉼표를 기준으로 나누겟다 하면 print(str.split(','))

# 특정문자의 인덱스 찾기 : find('문자'), index('문자')
# 찾고자 하는 문자가 "없을 때"
print(str.index('사'))
