'''
42587. 프로세스
https://school.programmers.co.kr/learn/courses/30/lessons/42587
15m 50s
'''

from collections import deque

def solution(priorities, location):
    q = deque()
    for i, v in enumerate(priorities):
        q.append((i, v))
    # print(q)
    
    # answer = []
    cnt = 0
    while q:
        _, max_v = max(q, key=lambda x: x[1])
        i, v = q.popleft()
        if v < max_v:
            q.append((i, v))
        else:
            # answer.append(i)
            cnt += 1
            if i == location:
                return cnt

    # return answer
    return -1

print()
print(solution([2, 1, 3, 2], 2))
print(1)

print()
print(solution([1, 1, 9, 1, 1, 1], 0))
print(5)