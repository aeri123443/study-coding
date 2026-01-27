'''
42583. lv2 다리를 지나는 트럭
https://school.programmers.co.kr/learn/courses/30/lessons/42583
다시 풀어보는거임 !!
'''

from collections import deque

def solution(bridge_length, weight, truck_weights):

    bridge = deque([0]*bridge_length)
    trucks = deque(truck_weights)
    answer = 0
    
    w_total = 0
    while trucks:
        # print()
        # print(w_total , trucks[0] , bridge[0])
        if w_total + trucks[0] - bridge[0] <= weight:
            # 새 트럭 넣기
            new_weight = trucks.popleft()
            bridge.append(new_weight)
            w_total += new_weight
        
        else: 
            bridge.append(0)

        # 다리 맨앞 요소 제거
        w_pop = bridge.popleft()
        w_total -= w_pop

        answer += 1
        # print('bridge', bridge)
        # print('trucks', trucks)

    return answer + bridge_length

print()
print(solution(2, 10, [7,4,5,6]))
print(8)

print()
print(solution(100, 100, [10]))
print(101)

print()
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
print(110)