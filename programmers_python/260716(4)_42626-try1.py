'''
42626. 더 맵게
https://school.programmers.co.kr/learn/courses/30/lessons/42626

문제 분석: 4m 42s
코드 작성: 9m 39s
디버깅: 0m 0s
total: 14m 21s
'''

import heapq

def solution(scoville, K):
    q = scoville[:]
    heapq.heapify(q)

    answer = 0
    while len(q) >= 2:
        if q[0] >= K: return answer

        a = heapq.heappop(q)
        b = heapq.heappop(q)
        heapq.heappush(q, a+b*2)
        answer+=1

    if q[0] >= K:
        return answer
    else:
        return -1

print(solution([1, 2, 3, 9, 10, 12], 7)) # 2
print(solution([1, 2, 3, 9, 10, 12], 1000)) # -1
