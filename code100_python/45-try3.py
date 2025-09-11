'''
p.463 45. 경주로 건설
https://school.programmers.co.kr/learn/courses/30/lessons/67259
- 최소비용이니 bfs 문제가 맞음
- visit는 어지간하면 큐에 쌓지 않고 관리하는 게 좋음
- '길이 겹칠 가능성' -> 이 경우 어떻게 처리할지 고민
'''

from collections import deque

def solution(board):
    size = len(board)
    # 0:x,  1:y
    move = [[1,0,0], [-1,0,0], [0,1,1], [0,-1,1]]

    q = deque()
    # [x][y][direction]
    visited_map = [[[float('inf'), float('inf')] for _ in range(size)] for _ in range(size)]
    q.append([0, 0, None, 0])
    visited_map[0][0][0] = 0
    visited_map[0][0][1] = 0
    min_cost = float('inf')
    while q:
        x, y, recent, cost = q.popleft()
        # print(x, y, recent, cost)

        if x==size-1 and y==size-1:
            min_cost = min(min_cost, cost)
        
        for dx, dy, change in move:
            nx, ny = x+dx, y+dy

            # 이동 가능 좌표 검사
            if nx>=0 and nx<size and ny>=0 and ny<size and board[nx][ny]==0:
                # 코너 추가 여부 검사
                # 비용 검사 후 큐 쌓기
                if change == recent or recent == None:
                    new_cost = cost + 100
                else: 
                    new_cost = cost + 100 + 500
                if visited_map[nx][ny][change]>new_cost and new_cost < min_cost:
                    visited_map[nx][ny][change] = new_cost
                    q.append([nx, ny, change, new_cost])

    return min_cost

# 900
print(solution([[0,1,1],[0,1,1],[0,0,0]]))
# 900
print(solution([[0,0,0],[0,0,0],[0,0,0]]))
# 3800
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
# 2100
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
# 3200
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))
