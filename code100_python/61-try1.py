'''
p.579 61. 지형 이동
https://school.programmers.co.kr/learn/courses/30/lessons/62050
소요시간: 159m 2s
실패 : 너무 복잡하게 생각함
'''

import heapq

def is_move(x, y, name):
    global visited, N
    return x >= 0 and y >= 0 and x < N and y < N and not name in visited

def solution(land, height):
    global visited, N
    N = len(land)
    node_num = N*N
    move = [[1,0], [-1,0], [0,1], [0,-1]]

    # 다익스트라
    # 노드 네임(0~node_num-1)으로 관리
    visited = set()
    q = []
    distance = {i:float('inf') for i in range(node_num)}
    recent = {i:i for i in range(node_num)}
    distance[0]=0

    heapq.heappush(q, [0, 0])

    while q:
        poped_dis, poped_name = heapq.heappop(q)
        print(poped_dis, poped_name)
        visited.add(poped_name)

        if poped_dis > distance[poped_name]: continue

        x, y = poped_name//N, poped_name%N
        for dx, dy in move:
            nx, ny = x+dx, y+dy
            n_name = N*nx+ny
            # print(n_name)
            if is_move(nx, ny, n_name):
                # print(nx, ny, n_name)
                if abs(land[x][y] - land[nx][ny]) <= height:
                    w = 0
                else:
                    w = abs(land[x][y] - land[nx][ny])
                if distance[n_name] > w + poped_dis:
                    print("  ", distance[n_name], "->", w + poped_dis)
                    print("  ", recent[n_name], "->", poped_name)
                    distance[n_name] = w + poped_dis
                    recent[n_name] = poped_name
                    heapq.heappush(q, [distance[n_name], n_name])
                    
    print(distance)
    print(recent)

    # 사다리 찾기
    answer = 0
    for i in range(1, node_num):
        # 이전 노드와 비교했을 때 비용이 달라지는 구간에서
        if distance[i-1] != distance[i]:
            # 이전 노드와의 높이 차이가 사다리 비용
            answer += distance[i] - distance[ recent[i] ]
    return answer

# 15
# print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3))
# 18
# print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 1))

print(solution([[1,3,5,7], [15,13,11,9], [17,19,21,23], [31,29,27,25]], 1))
