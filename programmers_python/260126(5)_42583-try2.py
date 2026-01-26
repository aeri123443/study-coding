'''
42583. 다리를 지나는 트럭
https://school.programmers.co.kr/learn/courses/30/lessons/42583
'''

from collections import deque

def solution(bridge_length, weight, truck_weights):
    q = deque(truck_weights)
    bridge_q = deque([0 for _ in range(bridge_length)])
    answer = 0
    total_w = 0

    while q:
        cur_truck = q[0]
        # 다음 턴에 트럭이 들어올 수 있으면, 브릿지에 트럭을 넣음
        if total_w + cur_truck - bridge_q[0] <= weight:
            bridge_q.append(cur_truck)
            q.popleft()
            total_w += cur_truck
        else:
            bridge_q.append(0)
        # 뭐든 들어갔으니 브릿지 앞쪽은 빼야함
        out_bridge = bridge_q.popleft()
        total_w -= out_bridge
        answer += 1

    # print(bridge_q)
    # bridge_q에 마지막 트럭이 담기는 순간 반복문이 종료되었을 것

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

# print()
# print(solution())
# print()