'''
121689. [PCCP 모의고사 #2] 3번 - 카페 확장
https://school.programmers.co.kr/learn/courses/15009/lessons/121689
'''

'''
0초에 손님 한 명이 가게에 도착하고, 정확히 k초마다 새로운 손님 한 명이 카페에 와서 줄을 섭니다. 
한 손님이 카페에서 나감과 동시에 다른 손님이 카페에 들어올 경우, 나가는 손님이 먼저 퇴장한 다음 들어오는 손님이 입장합니다.
오늘 카페에 동시에 존재한 손님 수의 최댓값을 return

q가 비어있을 때?
'''
from collections import deque

def solution(menu, order, k):
    t = 0
    next_t = menu[order[0]]
    order_idx = 0
    q = deque([menu[order[0]]]) # (음료 제작 시간)
    answer = 1
    
    for i in range(1, len(order)):
        t = i*k
        if t < next_t:
            q.append(menu[order[i]])
            answer = max(answer, len(q))
        else:
            while t >= next_t:
                q.popleft()
                if q:
                    next_t = next_t + q[0]
                else:
                    break
            if q:    
                q.append(menu[order[i]])
                answer = max(answer, len(q))
            else:
                q.append(menu[order[i]])
                next_t = t + menu[order[i]]
                answer = max(answer, len(q))
            
    return answer
