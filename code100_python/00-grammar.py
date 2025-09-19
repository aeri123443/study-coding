'''
리스트
'''

# 컴프리헨션 (List Comprehension)
# 1차원 리스트 생성
array = [i for i in range(20) if i%2==0]
# print(array)
array = [i*i for i in range(1,10)]
# print(array)

# 2차원 리스트 초기화
n = 3
m = 4
array = [[0]*m for i in range(n)]
# print(array)
# [[0,0,0,0],[0,0,0,0], [0,0,0,0]]

a = [1, 4, 3]
# 리스트 추가
a.append(2)
# 정렬
a.sort()
# 역순 정렬
a.sort(reverse=True)
# 리스트 역순
a.reverse 
# print(a) # [4, 3, 2, 1]
# 특정 인덱스에 데이터 추가
a.insert(1, 4)
# print(a) # [4, 0, 3, 2, 1]
# 특정 값인 데이터 개수 세기
# print(a.count(4))
# 특정 값 데이터 삭제
a.remove(2)
# print(a)
# 리스트 합치기
b = [9,8,7]
# print(a+b)

'''
딕셔너리
'''

data = {
    'a': 1,
    'b': 2,
    'c': 3
}

# 데이터 추가
data['d'] = 4

# 키/밸류 리스트
key_list = data.keys()
value_list = data.values()
# [print(key) for key in key_list]

'''
집합 자료형
'''

a = set([1,2,3,4,5])
b = {3,4,5,6,7}

# print(a|b) # 합집합
# print(a&b) # 교집합
# print(a-b) # 차집합

# 원소 추가
a.add(8)
# 여러 원소 추가 
a.update([3,9]) # 중복 원소는 업데이트 안됨
# 특정 원소 제거
a.remove(2)
# print(a)

'''
순열과 조합
'''

from itertools import permutations, combinations, product, combinations_with_replacement

data = ['a', 'b', 'c']
# 순열
result_permu = list( permutations(data, 3) )
# 조합
result_combi = list( combinations(data, 2) )
# 중복 순열
result_per_re = list( product( data, repeat=2))
# 중복 조합
result_combi_re = list(combinations_with_replacement( data, 2 ))
# print(result_permu)
# print(result_combi)
# print(result_per_re)
# print(result_combi_re)

'''
힙 - 학습 후 다시 보기
'''

# 힙 정렬
import heapq
def heapsort(iterable):
      h = []
      result = []
      for value in iterable:
              heapq.heappush(h, value)
      for i in range(len(h)):
              result.append(heapq.heappop(h))
      return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 부호를 사용하여 최대 힙(max heap) 구현
import heapq

def heapsort(iterable):
      h = []
      result = []
      for value in iterable:
              heapq.heappush(h, -value)
      for i in range(len(h)):
              result.append(-heapq.heappop(h))
      return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
#[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

'''
이진탐색
'''

from bisect import bisect_left, bisect_right

a = ['a', 'b', 'c', 'c', 'd', 'f']
x = 'c'
# 값이 특정 범위에 속하는 원소의 개수를 구하고자 할 때 사용
# 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾음
# print(bisect_left(a, x)) # 2
# 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾음
# print(bisect_right(a, x)) # 4

# print(bisect_left(a, 'f')) # 4
# print(bisect_left(a, 'e')) # 4
# print(bisect_left(a, 'g')) # 4


'''
스택, 큐
'''

from collections import deque

data = deque([1,2,3])
data.appendleft(1)
data.append(5)
# print(data)
data.pop()
data.popleft()
# print(data)

'''
수학
'''
import math

# print(math.factorial(5)) # 팩토리얼
# print(math.sqrt(20)) # 제곱근 square root
# print(math.gcd(3, 12)) # 최대공약수 greatest common divisor
# print(math.pi)
# print(math.e)
