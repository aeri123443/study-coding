'''
민트 초코 우유: 2025 상반기 오전 1번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/mint-choco-milk

문제 분석: 10m 27s
코드 1차 작성: 1h 31m 43s
최종 디버깅: 0m 0s
총 소요 시간: 1h 42m 11s
'''

from collections import deque

########################################
#### 전역 선언
########################################

MOVE = [(-1,0), (+1,0), (0,-1), (0,+1)]
INF = float('inf')

b_board = [] # 신앙심
item_board = [] # 신봉 음식
visited = []

N, T = -1, -1

########################################
#### 보조 함수
########################################

### 데이터 입력
def input_data():
    global N, T, b_board, item_board, visited
    item_to_bin = {'T': 0b100, 'C': 0b010, 'M': 0b001}

    N, T = map(int, input().split())
    item_board = [[item_to_bin[x] for x in list(input())] for _ in range(N)]
    b_board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]

### 그룹 및 대표자 선정
def bfs(sr, sc):
    represent = (b_board[sr][sc], -sr, -sc) # 신앙심 최대, r 최소, c 최소 (B, -r, -c)
    cnt = 1

    q = deque([(sr, sc)])
    item = item_board[sr][sc]
    visited[sr][sc] = True

    while q:
        cr, cc = q.popleft()

        for dr, dc in MOVE:
            nr, nc = dr+cr, dc+cc

            if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and item_board[nr][nc]==item:
                b = b_board[nr][nc]
                represent = max(represent, (b, -nr, -nc))
                visited[nr][nc] = True
                cnt += 1
                q.append((nr,nc))

    group_type = str(bin(item)).count('1')
    return cnt, group_type, represent[0], -represent[1], -represent[2]

########################################
#### 메인 로직
########################################
def main():
    answer = []

    # 0단계: 초기 데이터 입력
    input_data()
    # print()

    for _ in range(T):
        # 아침: 대표자 선정 이후 일괄 계산
        # 1단계: 점심

        ## 그룹 및 대표자 선정
        for i in range(N):
            for j in range(N):
                visited[i][j] = False

        represent = []
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    cnt, group_type, pb, pr, pc = bfs(i, j)

                    ## 대표자 추가 및 신앙심 업데이트
                    b_board[pr][pc] += cnt
                    represent.append((group_type, -b_board[pr][pc], pr, pc))

        # print()

        ## 2단계: 전파
        represent.sort() # 전파 순서

        # 전파당한 유무를 확인
        for i in range(N):
            for j in range(N):
                visited[i][j] = False

        for _, pb, pr, pc in represent:
            if visited[pr][pc]: continue
            pb = -pb

            x = pb-1
            b_board[pr][pc] = 1
            item = item_board[pr][pc]

            dr, dc = MOVE[pb%4]
            nr, nc= pr+dr, pc+dc

            while 0<=nr<N and 0<=nc<N and x > 0:
                # 아이템 다를 경우
                if item_board[nr][nc] != item:
                    y = b_board[nr][nc]
                    visited[nr][nc] = True
                    # 강한 전파
                    if x > y:
                        item_board[nr][nc] = item
                        x -= (y+1)
                        b_board[nr][nc] += 1
                    # 약한 전파
                    else:
                        # 디버깅 포인트: 비트연산 잘 되는지 확인
                        item_board[nr][nc] = (item_board[nr][nc] | item)
                        b_board[nr][nc] += x
                        x = 0

                nr += dr
                nc += dc

        # print()

        ## 3단계: 정답 계산
        daily_map = [0]*8
        sort_idx = [7, 6, 5, 3, 1, 2, 4]
        for i in range(N):
            for j in range(N):
                item = item_board[i][j]
                b = b_board[i][j]
                daily_map[item] += b

        answer.append(' '.join(map(str, [daily_map[idx] for idx in sort_idx])))
        # print()

    print('\n'.join(answer))

main()