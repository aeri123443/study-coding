'''
42583. 다리를 지나는 트럭
https://school.programmers.co.kr/learn/courses/30/lessons/42583

문제 분석: 12m 32s
코드 작성: 12m 23s
디버깅: 0m 0s
total: 24m 55s
'''

from collections import deque

def solution(bridge_length, weight, truck_weights):
    ready_q = deque(truck_weights) # 준비 큐
    running_q = deque([0], maxlen=bridge_length) # 실행 큐

    t = 0
    total_w = 0
    while ready_q:
        t += 1

        # 종료 프로세스 확인 및 total_w 업데이트
        if running_q[0] > 0:
            total_w -= running_q.popleft()

        # 대기 큐 -> 실행 큐 진입 가능하면 진입, total_w 업데이트
        if ready_q[0] + total_w <= weight:
            tmp = ready_q.popleft()
            running_q.append( tmp )
            total_w += tmp
        else: # 진입 불가하면 0 넣음
            running_q.append(0)

        # print(f't={t}')
        # print(f'ready_q={ready_q}')
        # print(f'running_q={running_q}')
        # print()

    return t + bridge_length

print(solution(2, 10, [7,4,5,6])) # 8
print(solution(100, 100, [10])) # 101
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10])) # 110
