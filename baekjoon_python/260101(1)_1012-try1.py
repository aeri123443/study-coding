'''
1012. <실버2> 유기농 배추
https://www.acmicpc.net/problem/1012
'''

from pprint import pprint

from collections import deque

board = []
visited = []
M, N, K = -1, -1, -1
move = [[0,1], [0,-1], [1,0], [-1,0]]

# 맵 초기화
def init_data():
    global board, visited, M, N, K
    board = []
    visited = []
    M, N, K = -1, -1, -1

# 시작 좌표 반환
def find_start_xy():
    global visited, M, N

    # visited 맵을 순환하며 방문하지 않은 좌표를 꺼냄
    for y in range(N):
        for x in range(M):
            if visited[y][x] == 'X' and board[y][x]==1:
                return (x,y)
            
    # 방문하지 않은 좌표가 없으면 false 반환        
    return False

# 이동 가능 좌표 확인
def is_possible(nx, ny):
    global M, N, visited

    # 범위 내의 좌표가 아니면 false
    if not (0<=nx<M and 0<=ny<N):
        return False
    # 방문한 좌표면 false
    if visited[ny][nx]=='O':
        return False
    
    return True

# bfs
def bfs(sx, sy):
    global board, visited, move

    # q: [sx, sy]
    q = deque([[sx, sy]])
    visited[sy][sx]='O'

    while q:

        x, y = q.popleft()

        # start 좌표 기준
        # 상하좌우로 이동해가며
        for dx, dy in move:
            nx, ny = x+dx, y+dy
            if is_possible(nx, ny) and board[ny][nx]==1:
                q.append([nx, ny])
                visited[ny][nx] = 'O'
            # 이동 가능 좌표 + 다음 좌표가 1이면 큐에 담음 / visited 표시

T = int(input())

for _ in range(T):
    init_data()
    answer = 0

    M, N, K = map(int, input().split())

    # 맵 생성
    board = [ [0]*M for _ in range(N) ]
    visited = [ ['X']*M for _ in range(N) ]

    # 1, 0 표시
    for _ in range(K):
        X, Y = map(int, input().split())
        board[Y][X] = 1
   
    while True:
        # 방문하지 않은 좌표에서 시작 좌표 추출
        sxy = find_start_xy()

        if not sxy: # false 값을 받았을 경우 (모든 맵 순환)
            print(answer)
            break

        (sx, sy) = sxy

        # answer 카운팅
        answer += 1
        # bfs 반복
        bfs(sx, sy)