'''
p.654 74. 2 x n 타일링
https://school.programmers.co.kr/learn/courses/30/lessons/12900
'''

def solution(n):
    arr = [0]*(n+1)
    arr[1] = 1
    arr[2] = 2

    for i in range(3, n+1):
        arr[i] = (arr[i-1] + arr[i-2]) % 1000000007
    return arr[-1]

# 5
print(solution(4))
# print(solution(999))
