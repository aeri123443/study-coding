'''
154538. 숫자 변환하기

https://school.programmers.co.kr/learn/courses/30/lessons/154538
'''

from collections import deque

def solution(x, y, n):
    if x==y: return 0

    visited = set()
    q = deque([(x, 0)])

    while q:
        num, cnt = q.popleft()

        for nxt in [num+n, num*2, num*3]:
            if nxt == y: return cnt+1

            if nxt not in visited and nxt < y:
                q.append( (nxt, cnt+1) )
                visited.add(nxt)

    return -1

print(solution(10,40,5)) # 2
print(solution(10,40,30)) # 1
print(solution(2,5,4)) # -1
