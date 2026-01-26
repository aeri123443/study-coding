'''
42583. 다리를 지나는 트럭
https://school.programmers.co.kr/learn/courses/30/lessons/42583
???? 뭐가 자꾸 틀리는데??? 다시해보자
'''

from collections import deque

def solution(bridge_length, weight, truck_weights):
    q = deque()
    
    q.append(truck_weights[0])
    answer = 1
    total_w = truck_weights[0]
    idx = 1
    cnt = 0  # 넘어간 트럭 수

    while cnt < len(truck_weights) or idx < len(truck_weights):

        # 1) 다음 트럭을 올릴 수 있으면 올리고, 아니면 0
        if idx < len(truck_weights) and total_w + truck_weights[idx] <= weight:
            q.append(truck_weights[idx])
            total_w += truck_weights[idx]
            idx += 1
        else:
            q.append(0)

        # 2) 다리 길이 초과하면 맨 앞 제거
        if len(q) > bridge_length:
            node_w = q.popleft()
            total_w -= node_w
            if node_w > 0:
                cnt += 1

        answer += 1

    return answer

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