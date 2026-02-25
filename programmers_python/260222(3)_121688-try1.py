'''
121688. [PCCP 모의고사 #2] 2번 - 신입사원 교육
https://school.programmers.co.kr/learn/courses/15009/lessons/121688
'''

'''
이때 한번 민수에게 선발된 사원이 다시 선발될 수도 있습니다. 
'''
# import math
# print(math.log10(1_000_000)*10_000)

import heapq

def solution(ability, number):
    q = []
    for a in ability:
        heapq.heappush(q, a)

    for _ in range(number):
        x = heapq.heappop(q)
        y = heapq.heappop(q)
        heapq.heappush(q, x+y)
        heapq.heappush(q, x+y)

    return sum(q)


