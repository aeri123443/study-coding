'''
138476. 귤 고르기
https://school.programmers.co.kr/learn/courses/30/lessons/138476

문제 분석: 2m 28s
코드 작성: 6m 59s
디버깅: 0m 0s
total: 9m 27s
'''
from collections import Counter

def solution(k, tangerine):
    counter_list = [ (k, v) for k, v in Counter(tangerine).items()]
    counter_list.sort(key=lambda x:-x[1])

    answer = 0 # 종류
    cur_picks = 0 # 현재까지 고른 귤 수
    for _, v in counter_list:
        answer += 1
        cur_picks += v
        if cur_picks >= k:
            return answer
    return answer

print(solution(6,	[1, 3, 2, 5, 4, 5, 2, 3])) # 3
print(solution(4,	[1, 3, 2, 5, 4, 5, 2, 3])) # 2
print(solution(2,	[1, 1, 1, 1, 2, 2, 2, 3])) # 1
