'''
p.610 67. 카펫
https://school.programmers.co.kr/learn/courses/30/lessons/42842
소요시간: 32m 21s
'''
import math

# 약수 조합 구하기
def dicisor(n):
    if n==1: return [[1,1]]
    if n==2: return [[2,1]]

    result = []
    for i in range(1, int(math.sqrt(n))+1):
        if n%i==0:
            result.append([n//i, i])
    return result

def solution(brown, yellow):
    dicisor_list = dicisor(yellow)

    for a, b in dicisor_list:
        if 2*(a+b+2) == brown:
            return [a+2,b+2]


# [4, 3]
print(solution(10, 2))
# [3, 3]
print(solution(8, 1))
# [8, 6]
print(solution(24, 24))

# [12, 3]
print(solution(26, 10))
# [7, 4]
print(solution(18, 10))
# [6, 6]
print(solution(20, 16))
# [10, 4]
print(solution(24, 16))
