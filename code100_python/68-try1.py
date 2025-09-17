'''
p.614 68. 점프와 순간 이동
https://school.programmers.co.kr/learn/courses/30/lessons/12980
소요시간: 39m 30s
문제 분석하는데 시간이 좀 걸림.. 
'''

def solution(n):
    return bin(n).count('1')

# 2
print(solution(5))
# 2
print(solution(6))
# 5
print(solution(5000))
# 3
print(solution(11))
# 2
print(solution(9))
# 1
print(solution(1))
# 1
print(solution(2))
