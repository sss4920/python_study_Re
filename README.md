# python_study
백준 풀이 및 공부내용입니다.

#runtime error 내용입니다.
### 공백으로 구분하기
```python
a, b = input().split(" ")
a = int(a)
b = int(b)
```
## 3일차 수업내용

### 문자열 실습
  * 문자열에서 ""와 ''를 배우고 둘이 섞어 쓸때는 " ' ' " 이런식으로 사용하는 것을 배움
  ```python
  sentence = "doesn\'t" # 이렇게 하면 작은 따옴표가 나옴 역슬레시는 escape 문자!
  sentence = 'doesn\'t' # 이런것도 그러므로 가능
  ```
  * 문자열에서 첫번째 따옴표 앞에 r을 추가하면 특수문자의 의미를 없앨 수 있다!
  ```python
  print(r'C:\some\name') # 문자열 앞에 r을 추가하므로써 \가 그냥 나온다! 에러안뜸
  ```
## 10/12 문제풀이
### 재귀 최대한도설정하기  
반복문 문제인 1065 한 수를 풀다가 새로운 에러인 재귀한도초과에러가 떴다. 그 해결책을 구글링해서 알아본 결과 
```python:
import sys  #sys모듈을 불러온뒤
sys.setrecursionlimit(10000)  #재귀의 한도를 10000까지 풀어주면 됩니다!
```
이와 같은 방법이 있다는 것을 알게 되었고 한도를 풀자마자 맞았습니다가 떠서 기분이 좋았던것 같당ㅠㅠ

  

