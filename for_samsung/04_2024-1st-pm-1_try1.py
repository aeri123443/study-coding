'''
마법의 숲 탐색: 2024 상반기 오후 1번 (L13)
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/magical-forest-exploration/description
소요시간: 3h 44m

[리뷰]
else는 정말 확실하게 '그 외'의 경우일 때만. 어지간하면 elif 쓰기
헷갈리지 말고 그냥 곱게 not (and and and) 이렇게 쓰자...
테스트 케이스! 생각할 시간 충분히 가지기!!

'''
from pprint import pprint

from collections import deque

R, C, K = map(int, input().split())
board = [[0]*C for _ in range(R)] 
visited = [[0]*C for _ in range(R)] 
di_map = {0:'N', 1:'E', 2:'S', 3:'W'}
move = [[-1,0], [0,1], [1,0], [0,-1]]
answer_list = []

#### 데이터 입력 및 초기화 ####

## 보드 초기화
def init_board():
    global board, C, R
    for r in range(R):
        for c in range(C):
            board[r][c]=0

## 방문 기록 초기화
def init_visited():
    global visited, R, C
    for r in range(R):
        for c in range(C):
            visited[r][c]=False
#### 골렘 이동 ####

## 골렘 이동 가능 판정 함수(다음 좌표 리스트)
# 다음 좌표가 벽에 막히는지, 골렘에 막히는지 파악
def can_gol(i, j, d):
    global board, R, C
    
    # 다음 좌표 담기
    next_list = []
    if d==2: # 남쪽
        next_list = [[i+1, j-1], [i+2, j], [i+1, j+1]]
    elif d==3: # 서쪽
        next_list = [[i-1, j-1], [i, j-2], [i+1, j-1], [i+1, j-2], [i+2, j-1]]
    elif d==1: # 동쪽
        next_list = [[i-1, j+1], [i, j+2], [i+1, j+1], [i+1, j+2], [i+2, j+1]]

    for ni, nj in next_list:
        if nj>=0 and ni<R and nj<C and board[ni][nj]==0:
            continue
        else: 
            if ni < 0 and nj >= 0:
                continue
            else:
                return False
    return True

#### 골렘 이동 ####
## 이동 가능 기준: 벽이나 골렘이 있는가?
def move_gol(cur_r, cur_c, cur_d):
    global board, move

    while True:
        # print(cur_r, cur_c, cur_d)

        ## 남쪽 이동
        if can_gol(cur_r, cur_c, 2):
            # print('남쪽 이동')
            cur_r += 1
        ## 안되면 서쪽 이동
        elif can_gol(cur_r, cur_c, 3):
            # 서+남 한번에 이동 후 회전 정보 저장
            # print('서쪽 이동')

            cur_r += 1
            cur_c -= 1
            cur_d -= 1
            if cur_d==-1: cur_d=3
        ## 안되면 동쪽 이동
        elif can_gol(cur_r, cur_c, 1):
            # 동+남 한번에 이동 후 회전 정보 저장
            # print('동쪽 이동')

            cur_r += 1
            cur_c += 1
            cur_d += 1
            if cur_d==4: cur_d=0
        ## 남/서/동 이동 모두 안된다면...!!
        else: 
            # print('남/서/동 이동 모두 안된다면...!!')

            ## 안되면 숲 안쪽인지 검사 
            # 숲 안쪽이면 골렘 고정, 요정 이동 단계로
            if cur_r >= 1:
                gol_name = i*2+1
                gol_exit = gol_name+1

                board[cur_r][cur_c] = gol_name
                for dr, dc in move:
                    nnr, nnc = dr+cur_r, dc+cur_c
                    board[nnr][nnc] = gol_name

                ddr, ddc = move[ cur_d ]
                nnr, nnc = ddr+cur_r, ddc+cur_c
                board[nnr][nnc] = gol_exit
                return [cur_r, cur_c, gol_name]
            # 숲 바깥쪽이면 모든 골렘 제거
            else:
                init_board()
                return [-1, -1, -1]

#### 요정 이동 ####

# 출구 검사 및 bfs
def move_elf(sr, sc, sg):
    global answer_list, board, visited, move, R ,C

    max_r = -1
    q = deque()
    q.append([sr, sc, sg])
    # 출구가 다른 골렘과 연결되었는지 확인
    # 연결되었다면 출구 방향으로 이동

    while q:
        r, c, g = q.popleft()

        # 상하좌우로 이동
        for dr, dc in move:
            nr, nc = r+dr, c+dc
            ng = g
            # print(nr, nc, ng)

            # 이동 불가 좌표(오류 방지), 방문한 좌표면 패스
            if not (nr>=0 and nc>=0 and nr<R and nc<C and not visited[nr][nc]):
                continue

            # 골렘 넘어가면 패스
            if board[nr][nc] == 0:
                continue

            # 다른 골렘인데 
            if not (board[nr][nc] == g or board[nr][nc] == g+1):
                # 지금 위치가 출구면 골렘 번호 변경
                if board[r][c] == g+1:
                    # 다음 위치가 다른 골렘의 출구였을 경우, 그 골렘번호로
                    if board[nr][nc]%2 == 0:
                        ng = board[nr][nc] -1
                    else: ng = board[nr][nc]
                # 지금 위치가 출구가 아니면 막힘(짝수)
                else:
                    continue
            
            # 가장 큰 행값 저장
            max_r = max(max_r, nr)
            # 방문처리 후 큐에 쌓기
            visited[nr][nc] = True
            q.append([nr, nc, ng])

    ## 결과 누적
    # 확인용으로 리스트를 만들고 한 번에 더하기 (1씩 더하는거 잊지 않기)
    answer_list.append(max_r+1)

    return max_r

#### main ####

for i in range(K):
    # print()
    c, d = map(int, input().split())

    # 요정 좌표 (골렘 중앙)
    cur_c, cur_r, cur_d = c-1, -2, d
    cur_r, cur_c, gol_name = move_gol(cur_r, cur_c, cur_d)

    # pprint('move_gol...')
    # print(i, cur_r, cur_c)
    # pprint(board)

    if (-1,-1,-1) == (cur_r, cur_c, gol_name):
        continue


    #### 요정 이동 ####
    # 출구 검사 및 bfs
    tmp_maxr = move_elf(cur_r, cur_c, gol_name)
    # print(tmp_maxr)

    #### 데이터 초기화 ####
    init_visited()

#### 결과 출력 ####
# print(answer_list)
print(sum(answer_list))
