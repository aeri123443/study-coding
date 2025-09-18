'''
p.652 73. 피보나치 수
https://school.programmers.co.kr/learn/courses/30/lessons/12945
소요시간: 9m 47s
'''

def solution(n):
    arr = [0]*(n+1)
    arr[1] = 1

    for i in range(2, n+1):
        arr[i] = arr[i-2] + arr[i-1]

    return arr[-1] % 1234567

# 2
print(solution(3))
# 5
print(solution(5))
