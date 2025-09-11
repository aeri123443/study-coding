'''
p.463 45. 경주로 건설
https://school.programmers.co.kr/learn/courses/30/lessons/67259
소요시간: 58m 52s, 시간초과 68/100
'''

from collections import deque

def solution(board):
    size = len(board)
    move = [[1,0,'x'], [-1,0,'x'], [0,1,'y'], [0,-1,'y']]

    q = deque()
    # visited_map = [[False]*size for _ in range(size)]
    q.append([0, 0, None, 0, 0, {' '.join(str([0, 0]))}])
    min_cost = float('inf')
    while q:
        x, y, recent, straight, corner, visited = q.popleft()
        # print(x, y, straight, corner)

        if x==size-1 and y==size-1:
            min_cost = min(min_cost, straight*100 + corner*500)
        
        for dx, dy, change in move:
            nx, ny = x+dx, y+dy

            # 이동 가능 좌표 검사
            if nx>=0 and nx<size and ny>=0 and ny<size:
                if board[nx][ny]==0 and not ' '.join(str([nx, ny])) in visited:
                    # 코너 추가 여부 검사
                    # 비용 검사 후 큐 쌓기
                    if change == recent or recent == None:
                        cost = corner*500 + (straight+1)*100
                        new_corner = corner
                    else: 
                        cost = (corner+1)*500 + (straight+1)*100
                        new_corner = corner+1 
                    if cost < min_cost:
                        new_visited = set(visited)
                        new_visited.update([' '.join(str([nx, ny]))])
                        q.append([nx, ny, change, straight+1, new_corner, new_visited])

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
