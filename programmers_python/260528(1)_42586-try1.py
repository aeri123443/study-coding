'''
42586. 기능 개발
https://school.programmers.co.kr/learn/courses/30/lessons/42586

문제 분석: 6m 46s
코드 작성: 6m 28s
디버깅: 0m 0s
total: 13m 14s
'''
import math

def solution(progresses, speeds):

    req_days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    # print(req_days)

    today = 0
    answer = []
    stack = 0
    for rd in req_days:
        if today < rd:
            answer.append(1)
            today = rd
        else:
            answer[-1] += 1
        # print(rd, answer)
    return answer

# [2, 1]
print(solution([93, 30, 55], [1, 30, 5]))

# [1, 3, 2]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
