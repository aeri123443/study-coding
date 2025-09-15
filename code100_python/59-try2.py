'''
p.572 59. 가장 큰 수
https://school.programmers.co.kr/learn/courses/30/lessons/42746
cmp_to_key 활용해보기
'''

from functools import cmp_to_key

# a, b: 문자열 타입의 숫자
def compare(a, b):
    int1,int2 = int(a+b), int(b+a)
    if int1>int2: return -1
    elif int1<int2: return 1
    else: return 0

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare))

    answer = ''.join(numbers)
    return '0' if answer[0]=='0' else answer

# '9534330'
print(solution([3, 30, 34, 5, 9]))
# '6210'
print(solution([6, 10, 2]))
# '6111110'
print(solution([6, 110, 11, 1]))
# '6111100'
print(solution([1, 100, 11, 6]))
# '0'
print(solution([0,0,0,0]))
