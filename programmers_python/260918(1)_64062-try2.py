'''
64062. 2019 카카오 개발자 겨울 인턴십 - 징검다리 건너기
https://school.programmers.co.kr/learn/courses/30/lessons/64062


'''
from collections import deque

def solution(stones, k):
    q = deque()
    n = len(stones)
    if n==k:
        return max(stones)

    answer = float('inf')

    for i, v in enumerate(stones):
        while q and q[-1][1] < v:
            q.pop()
        q.append((i,v))

        if q[0][0] <= i-k:
            q.popleft()

        if i >= k-1:
            answer = min(answer, q[0][1])

    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)) #3
print(solution([4,9,7,5,3,5,6,8,4,2,7,9], 5)) #7
