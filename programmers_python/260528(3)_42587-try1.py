'''
42587. 프로세스
https://school.programmers.co.kr/learn/courses/30/lessons/42587

문제 분석: 4m 9s
코드 작성: 6m 9s
디버깅: 0m 0s
total: 10m 18s
'''

'''
1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
  3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.
'''

from collections import deque

def solution(priorities, location):
    sorted_p = sorted(priorities)
    q = deque( [ (v, i) for i, v in enumerate(priorities) ])
    # print(q, sorted_p)
    answer = 0

    while q:
        v, idx = q.popleft()
        if v == sorted_p[-1]:
            answer += 1
            if idx == location: return answer
            sorted_p.pop()
        else:
            q.append( (v, idx) )

    return answer

print(solution([2, 1, 3, 2], 2)) # 1
print(solution([1, 1, 9, 1, 1, 1], 0)) # 5
