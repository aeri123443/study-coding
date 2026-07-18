'''
12953. N개의 최소공배수
https://school.programmers.co.kr/learn/courses/30/lessons/12953

문제 분석: 1m 50s
코드 작성: 8m 57s
디버깅: 0m 0s
total: 10m 47s
'''

# 두 수의 최대공약수
def gcd(a, b):
    while b > 0:
        q, r = divmod(a, b)
        a, b = b, r
    return a

# 두 수의 최소공배수
def lcm(a, b):
    return (a*b) // gcd(a, b)

def solution(arr):
    answer = arr[0]
    for i in range(1, len(arr)):
        answer = lcm(answer, arr[i])

    return answer

print(solution([2,6,8,14])) #168
print(solution([1,2,3])) #6
