'''
AI 로봇청소기:  2025 하반기 오후 1번 문제
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/ai-robot

문제 분석: 13m 32s
코드 작성: 2h 07m 19s
최종 디버깅: 3m 02s

총 소요 시간: 2h 23m 54s

시간 오버 포인트
1. find_robot_move() 에서 로봇의 위치에 먼지가 있을 경우 (거리가 0) 이동하지 않는 경우를 고려하지 않음
   -> 아니 왜 헷갈리게 초기 위치에 먼지가 없음을 보장한다는 소릴 써둔건데 ㅡㅡ
   -> 공개 케이스2를 일일이 확인하느라 시간을 너무 오래 씀
2. 먼지 확산은 4방향 합을 10으로 나누는 거라서 4방향의 합에 따라 몫이 달라질 수 있는데, 이걸 간과하고 먼지 기준 4방향에 대해 먼지량 누적값을 반환함
   -> 공개 케이스2를 일일이 확인하느라 시간을 너무 오래 씀

오류 포인트
1. find_robot_move() 에서 로봇이 이동 불가할 경우 (INF, INF)를 반환하면서, 다음 단계에서 실수 좌표를 사용했다는 에러가 발생
'''
from collections import deque

################################################
#### 전역 선언
################################################
INF = float('inf')
MOVE = [(0,+1), (+1,0), (0,-1), (-1,0)]

N, K, L = -1, -1, -1
item_board = [] # 먼지, 물건이 있는 보드
robot_board = [] # 로봇의 위치가 있는 보드
robots = [] # 각 로봇의 좌표 정보

################################################
#### 보조 함수
################################################
def input_data():
    global N, K, L, robots, item_board, robot_board

    N, K, L = map(int, input().split())
    item_board = [list(map(int, input().split())) for _ in range(N)]
    robot_board = [ [-1]*N for _ in range(N)]

    for i in range(K):
        r, c = map(int, input().split())
        r -= 1
        c -= 1

        robots.append((r, c))
        robot_board[r][c] = i

# 로봇이 이동할 좌표 선정 (bfs)
def find_robot_move(num, sr, sc):
    if item_board[sr][sc] > 0:
        return sr, sc

    min_info = (INF, INF, INF) # 거리, 행, 열

    q = deque([(sr, sc, 0)])
    visited = {(sr, sc)}

    while q:
        cr, cc, cnt = q.popleft()

        for dr, dc in MOVE:
            nr, nc = cr+dr, cc+dc

            # 범위내, 장애물, 방문여부
            if 0<=nr<N and 0<=nc<N and item_board[nr][nc] >= 0 and (nr, nc) not in visited:
                # 로봇보드는 따로 체크 (-1이거나, 자신을 제외한 0 이상의 숫자가 아니거나(==자기자신))
                if robot_board[nr][nc] == -1 or robot_board[nr][nc] == num:

                    if cnt+1 > min_info[0]: continue

                    # 다음 위치에 먼지가 있을 경우, min_info 업데이트
                    if item_board[nr][nc] >= 1:
                        min_info = min( min_info, (cnt+1, nr, nc) )

                    q.append( (nr, nc, cnt+1) )
                    visited.add( (nr,nc) )

    if min_info[0] == INF:
        return sr, sc

    return min_info[1], min_info[2]

# 청소할 방향 선정 (격자 당 최대 20 고려)
# 좌표 및 제거량(-) 반환
def find_robot_d(r, c):
    max_val = -INF
    max_d = -1

    # 청소할 방향 선정
    for d in range(4):
        tmp_val = 0
        for dd in range(4):
            # 반대 방향 빼고 탐색
            if dd == (d-2)%4: continue
            dr, dc = MOVE[dd]
            # 청소 가능한 연기량 합 구하고 (20 최대)
            nr, nc = dr+r, dc+c
            if 0<=nr<N and 0<=nc<N and item_board[nr][nc]>0:
                tmp_val += min(item_board[nr][nc], 20)
        # print(tmp_val, max_val)
        if max_val < tmp_val:
            max_val = tmp_val
            max_d = d
        # print(max_val, max_d)
    # 좌표 및 제거량 반환, 해당 위치에 먼지가 있을 때에만 반영
    remove_target = [(r, c, -min(item_board[r][c], 20))] if item_board[r][c] > 0 else []

    for d in range(4):
        if max_d == (d-2)%4: continue

        dr, dc = MOVE[d]
        nr, nc = r+dr, c+dc

        if 0 <= nr < N and 0 <= nc < N and item_board[nr][nc] > 0:
            remove_target.append( (nr, nc, -min(item_board[nr][nc], 20)) )

    return remove_target

# 먼지 좌표 및 추가 먼지량 반환
def find_dust():
    add_target = []

    # 빈 격자 기준, 주변 4방향에 대해 먼지 확산량 업데이트
    for i in range(N):
        for j in range(N):
            if item_board[i][j] != 0: continue
            tmp_val = 0
            for di, dj in MOVE:
                ni, nj = di + i, dj + j
                if 0 <= ni < N and 0 <= nj < N and item_board[ni][nj] > 0:
                    tmp_val += item_board[ni][nj]
            add_target.append((i, j, tmp_val//10))

    return add_target
# 먼지량 업데이트 (청소, 누적, 확산)
def update_dust(arr):
    for r, c, val in arr:
        item_board[r][c] += val

# 먼지량 계산
def cal_dust():
    result = 0
    for i in range(N):
        for j in range(N):
            if item_board[i][j]>0:
                result += item_board[i][j]
    return result
################################################
#### 메인 로직
################################################
def main():
    answer = []
    # 0단계: 데이터 입력
    input_data()
    # print()
    for _ in range(L):
        # 1단계: 로봇 이동
        for num in range(K):
            ## 1-1: 이동할 좌표 선정
            sr, sc = robots[num]
            tr, tc = find_robot_move(num, sr, sc)
            # print()
            ## 1-2: 로봇 이동
            robot_board[sr][sc] = -1
            robot_board[tr][tc] = num
            robots[num] = (tr, tc)
        # print()

        # 2단계: 청소
        for num in range(K):
            ## 2-1: 청소할 방향 선정 (격자 당 최대 20 고려)
            sr, sc = robots[num]
            remove_target = find_robot_d(sr, sc)
            # print()

            ## 2-2: 청소
            update_dust(remove_target)
        # print()

        # 3단계: 먼지 축적
        for i in range(N):
            for j in range(N):
                if item_board[i][j] > 0:
                    item_board[i][j] += 5
        # print()

        # 4단계: 먼지 확산
        ## 4-1: 먼지 좌표 및 먼지량 반환
        add_target = find_dust()
        # print()
        ## 4-2: 먼지 좌표 기준 먼지 제거
        update_dust(add_target)
        # print()

        # 5단계: 먼지량 계산
        answer.append(str(cal_dust()))
        # print()
    print('\n'.join(answer))

if __name__ == '__main__':
    main()
