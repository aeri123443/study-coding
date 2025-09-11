'''
p.463 45. 경주로 건설
https://school.programmers.co.kr/learn/courses/30/lessons/67259
소요시간: 58m 52s -> 64m 52s, 시간초과 72/100
dfs로 바꿔보기
'''

def solution(board):
    global size, min_cost
    size = len(board)
    move = [[1,0,'x'], [-1,0,'x'], [0,1,'y'], [0,-1,'y']]
    min_cost = float('inf')

    def dfs(x, y, recent, straight, corner, visited):
        global size, min_cost
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
                        dfs(nx, ny, change, straight+1, new_corner, new_visited)
    dfs(0, 0, None, 0, 0, {' '.join(str([0, 0]))})
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
