'''
12980. 점프와 순간 이동
https://school.programmers.co.kr/learn/courses/30/lessons/12980

문제 분석: 8m 12s
코드 작성: 2m 13s
디버깅: 0m 0s
total: 10m 25s
'''


def solution(n):
    answer = 0
    for x in str(bin(n)):
        if x == '1': answer += 1

    return answer

print(solution(5))
print(solution(6))
print(solution(5000))
