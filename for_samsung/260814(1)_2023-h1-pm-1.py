'''
메이즈 러너: 2023 상반기 오후 1번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/maze-runner/description

문제 분석: 14m 34s
코드 작성: 2h 32m 19s
  - [시간 소요] 처음에는 참가자의 좌표 상태는 people에서만 관리하면 될 줄 알았는데, 미로 회전 사각형을 구하는 과정에서 사람 좌표도 2차원 보드 관리가 필요하다는 걸 알았음
             -> 이에 people_board 추가
  - [시간 소요] find_square_candidate를 찾고, 그들을 포함한 최종 정사각형을 구하는 과정에서, O(n^2)*O(n^2)로 하나씩 살펴보는 것 말고 다른 효율적인 방법이 있을지 고민
             -> 사람과 출구의 max 좌표를 사각형의 끝 좌표로 잡고, 역산하여 좌측상단 좌표를 구함
  - [시간 소요] 처음엔 단순히 zip으로 회전만 시켰는데, 생각해보니 people list와 출구 좌표도 회전시켜야 했음. zip이 아니라 직접 좌표를 계산해야할지 고민
             -> 어차피 tmp board를 실제 보드에 담는 과정에서 tmp board의 모든 좌표를 읽고 있으니까, 이때 그냥 각 좌표에 대해 참가자나 출구가 있으면 업데이트 시키는 코드를 끼워넣어도 괜찮겠다고 판단
  - [시간 소요] 조기 종료 조건에만 집중해서(+디버깅 목적) 탈출한 사람의 이동 횟수만 담고 나중에 sum하려고 했는데, 문제 다시 읽어보니 모든 참가자의 이동 횟수였음
             -> ans=[]에 탈출한 사람 이동 횟수 담는 로직에서, arrived cnt를 업데이트하는 로직으로 변경
  - [시간 소요] move people에서 prev_dis > cal_dis(er, ec, nr, nc)라고 해야 했는데 복붙 후 수정 실수로 cal_dis(r, c, nr, nc)라고 써서 로직에 오류 발생, 디버깅 시간이 좀 걸림
최종 디버깅: 0m 0s

총 소요 시간: 2h 46m 53s
'''
from collections import deque

# =============================================
# 전역 선언부
# =============================================

N, M, K = -1, -1, -1
INF = float('inf')

ex = (-1, -1) # (r, c)
MOVE = [(-1,0), (+1, 0), (0,-1), (0,+1), (-1,-1), (-1,+1), (+1,+1), (+1,-1)] # 상하좌우, +대각

people = [(-1,-1,0, True)] # (r, c, 이동 횟수, 도착 여부)
board = []
people_board = []

# =============================================
# 보조 함수
# =============================================

# 디버깅 프린트
def debug_print(t):
    tmp = [[set() for _ in range(N)] for _ in range(N)]

    print(f'\ndebug {t} seconds')

    for idx, (r, c, n, a) in enumerate(people):
        if idx == 0: continue
        print(f'{idx}: ({r}, {c}), moved {n}, arrived {a}')
        tmp[r][c].add(idx)

    tmp[ex[0]][ex[1]] = '{-}'
    for i in range(N):
        for j in range(N):
            if not tmp[i][j]: tmp[i][j] = '{ }'

    print('\npeople and exit')
    print('\n'.join([('\t'.join(map(str, x))) for x in tmp]))
    print('\nmap')
    print('\n'.join([(' '.join(map(str, x))) for x in board]))

# 초기 데이터 입력
def input_data():
    global N, M, K, people, board, people_board, ex

    N, M, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    people_board = [[set() for _ in range(N)] for _ in range(N)]

    for idx in range(1, M+1):
        r, c = map(lambda x: int(x)-1, input().split())
        people_board[r][c].add(idx)
        people.append((r, c, 0, False))

    ex = tuple(map(lambda x: int(x)-1, input().split()))

# 범위 확인
def is_range(r, c):
    return 0<=r<N and 0<=c<N

# 거리 반환
def cal_dis(r1, c1, r2, c2):
    return abs(r1-r2) + abs(c1-c2)

# 참가자 이동
def move_people():
    er, ec = ex
    arrived_people = set()

    for idx, (r, c, cnt, arrived) in enumerate(people):
        if arrived: continue

        prev_dis = cal_dis(r, c, er, ec)

        for dr, dc in MOVE[:4]:
            nr, nc = dr+r, dc+c
            if is_range(nr, nc) and board[nr][nc] == 0 and prev_dis > cal_dis(er, ec, nr, nc):
                nar = ((er, ec) == (nr, nc))
                people[idx] = (nr, nc, cnt+1, nar)
                people_board[r][c].remove(idx)
                if nar:
                    arrived_people.add(idx)
                else:
                    people_board[nr][nc].add(idx)
                # print()
                break

    return arrived_people


# 가장 작은 정사각형 후보 찾기
# 좌측 상단 좌표와 범위 안에 들어갈 사용자의 좌표를 반환
def find_square_candidate():
    min_cnt = INF # 한 변의 길이
    min_pos = set() # 한 변의 길이가 최소를 만족하게 하는 사용자 위치 목록 (r, c)
    er, ec = ex

    q = deque([(er, ec)])
    visited = [[-1]*N for _ in range(N)]
    visited[er][ec] = 0

    while q:
        cr, cc = q.popleft()

        if visited[cr][cc] > min_cnt:
            continue

        for dr, dc in MOVE:
            nr, nc = dr+cr, dc+cc
            ncnt = visited[cr][cc] + 1
            if is_range(nr, nc) and visited[nr][nc] == -1:
                visited[nr][nc] = ncnt
                q.append((nr, nc))

                if people_board[nr][nc]:
                    if min_cnt == ncnt:
                        min_pos.add((nr, nc))
                    elif min_cnt > ncnt:
                        min_cnt = ncnt
                        min_pos = {(nr, nc)}

    return min_cnt, min_pos

# min_pos와 출구를 기준으로, 가장 작은 정사각형의 좌측 상단 좌표를 찾기
def find_square(cnt, pos):
    min_square = (INF, INF) # r, c
    er, ec = ex

    for r, c in pos:
        sq_er = max(r, er)
        sq_ec = max(c, ec)

        sr = max(0, sq_er-cnt)
        sc = max(0, sq_ec-cnt)

        min_square = min(min_square, (sr, sc))

    return min_square

# 내구도 감소 및 회전
def rotate(cnt, sr, sc):
    global ex

    er, ec = sr+cnt+1, sc+cnt+1

    # 내구도를 감소시킨 후 임시 배열에 넣음
    tmp_map_board = []
    for r in range(sr, er):
        tmp_line = []
        for c in range(sc, ec):
            tmp_line.append(max(board[r][c] - 1, 0))
        tmp_map_board.append(tmp_line)

    # 사람 임시배열에 출구 넣음 (출구에 벽이 있을 수 있으므로, board 기록하면 겹칠 수 있음)
    tmp_people_board = [line[sc:ec][:] for line in people_board[sr:er]]
    tmp_people_board[ex[0]-sr][ex[1]-sc] = -1

    # 회전
    tmp_map_rotate = [x[::-1] for x in zip(*tmp_map_board)]
    tmp_people_rotate = [x[::-1] for x in zip(*tmp_people_board)]

    # 회전 결과를 업데이트 하면서, 출구와 참가자의 정보도 업데이트!
    for i in range(cnt+1):
        for j in range(cnt+1):
            nr, nc = i+sr, j+sc
            if tmp_people_rotate[i][j]:
                if tmp_people_rotate[i][j] == -1: #출구
                    ex = (nr, nc)
                else: # 사람
                    for p_idx in tmp_people_rotate[i][j]:
                        _, _, pcnt, par = people[p_idx]
                        people[p_idx] = (nr, nc, pcnt, par)

            people_board[nr][nc] = tmp_people_rotate[i][j] if tmp_people_rotate[i][j] != -1 else set()
            board[nr][nc] = tmp_map_rotate[i][j]


# =============================================
# 메인 로직
# =============================================
def main():
    # ===========================
    # 0. 초기 데이터 입력
    # ===========================
    input_data()
    # debug_print(0)
    # print()

    arrived_cnt = 0
    for t in range(K):

        # ===========================
        # 1. 참가자 이동
        # ===========================

        # 이동할 수 있는 참가자들의 다음 좌표를 반환
        arrived_people = move_people()
        arrived_cnt += len(arrived_people)

        # print()
        # 모든 참가자가 탈출하면 종료
        if arrived_cnt == M: break

        # ===========================
        # 2. 미로 회전
        # ===========================

        # 가장 작은 정사각형 찾기

        # 좌측 상단 좌표와 범위 안에 들어갈 사용자의 좌표를 반환
        min_cnt, min_pos = find_square_candidate()
        # print()
        # min_pos와 출구를 기준으로, 가장 작은 정사각형의 좌측 상단 좌표를 찾기
        sr, sc = find_square(min_cnt, min_pos)
        # print()
        # 내구도 감소 및 회전
        rotate(min_cnt, sr, sc)
        # debug_print(t)
        # print()

    move_cnt = 0
    for _, _, cnt, _ in people:
        move_cnt += cnt

    print(f'{move_cnt}\n{ex[0]+1} {ex[1]+1}')
    # print()
main()