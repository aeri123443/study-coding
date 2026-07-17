'''
154538. 숫자 변환하기
https://school.programmers.co.kr/learn/courses/30/lessons/154538

문제 분석: 3m 25s
코드 작성: 15m 7s
디버깅: 2m 52s -> BFS에서 실수로 visited.add를 안 함
total: 21m 24s
'''
from collections import deque

# 다음 값이 유효한지 확인 후 큐에 넣음
# True: 값이 일치함, False: 값이 일치하지 않음 (큐에 들어가거나 안 들어가거나..)
def validation_and_push(num, y, cnt, visited, q):
    if num == y:
        return True

    if num not in visited and num < y:
        q.append((num, cnt + 1))
        visited.add(num)
    return False

def solution(x, y, n):
    visited = {x}
    q = deque([(x, 0)])

    if x==y: return 0

    while q:
        cur, cnt = q.popleft()

        a = cur + n
        b = cur * 2
        c = cur * 3

        if validation_and_push(a, y, cnt, visited, q): return cnt + 1
        if validation_and_push(b, y, cnt, visited, q): return cnt + 1
        if validation_and_push(c, y, cnt, visited, q): return cnt + 1

    return -1

print(solution(10,	40,	5)) # 2
print(solution(10,	40,	30)) # 1
print(solution(2,	5,	4)) # -1
print(solution(2,	2,	4)) # 0
print(solution(1,	1000000,	1)) # 19
