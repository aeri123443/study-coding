
# 1회독 2:30
# 2회독 4:31
# 설계 51:03 +  (방문불가판정 아이디어 내는게 좀 오래 걸림)
# 큐 쓰는 bfs에서 스택 관리하는 bfs로 변경, 표 작성 17:40 + 0:56
# tc fail 디버깅: return turn+1 -> return turn 고쳤었는데 이걸 한 군데에서만 고침;; 디버깅 11:37
# tc fail 디버깅: r 계산할 때 %로 안 줄여줌; 디버깅 6:26
# 총 소요시간 3:24:31

# [!] -1 반환 케이스 확인
# [!] 5*5 맵에서 극단적으로 100턴 방황하다가 100턴 후에 회전하면서 탈출이 가능해진 경우
#     -> 마지막 회전 명령이 끝난 후 (전체 영역 넓이) 시간 후에도 도착한 애가 없으면 종료

# 회전 T번 (200)
# - 최대 턴: T + M + 1
# 시간복잡도 (T+M+1) * (M)
# 공간복잡도 (r,c,turn) -> (M*(T+M+1))
# 50*251
from collections import defaultdict

DEBUG = False
N, T = map(int, input().split())
M = (N+1)//2
max_turn = T+((N*N)+1)//2+3
MOVE = [(-1,0), (-1,+1), (0,+1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)] # 시계
zero_one_board = [list(map(int, input().split())) for _ in range(N)]
area_board = [[0]*N for _ in range(N)]
path_by_area = {} # 영역별 path {영역: [ , , ..]}
potal_list = [tuple(map(lambda x:int(x)-1, input().split())) for _ in range(M)]
rot_cmd = [list(map(int, input().split())) for _ in range(T)] # 변형 예정 {turn: {x: r*d}}

# 전역 작성 11:23

# 회전 명령 모으기
# 회전 명령 dict 변환
#     - t x d r, t턴에 x번 영역이 d 방향으로 r만큼 회전
#     - 한 턴에 여러번 회전 가능, 입력순서대로 회전
def preprocess_rot_cmd(): # 6:6
    global rot_cmd

    tmp = {}
    for t, x, d, r in  rot_cmd:
        if t not in tmp:
            tmp[t] = defaultdict(int)

        tmp[t][x] += r*d

    # 최종 r 값을 path 길이에 따라 변환 -> 이부분 두번째 디버깅/..
    for t in tmp:
        for area, r in tmp[t].items():
            tmp[t][area] = r % len(path_by_area[area])

    rot_cmd = tmp

# path_by_area 업데이트
# area_board 업데이트
def update_area_info(): # 13:32
    path_by_area[1] = [(M-1, M-1)]
    area_board[M-1][M-1] = 1

    for m in range(2, M+1):
        p = []
        cr, cc = M-m , M-1

        for d in [3, 5, 7, 1]:
            dr, dc = MOVE[d]
            for _ in range(m-1):
                p.append((cr, cc))
                area_board[cr][cc] = m

                cr+=dr
                cc+=dc

        path_by_area[m] = p

# 탈출구/포털 정보 업데이트
# 탈출구/포털이 0 위치에 있으면 out
def update_potal(): # 3:24
    for r,c in potal_list:
        if zero_one_board[r][c] == 0:
            return False
        else: zero_one_board[r][c] = -1

    return True

# 회전 수행
# pos 반환, path 수정, 0-1 보드 회전
def rotate(turn, cur_pos):
    global zero_one_board
    new_pos = []
    new_board = [[0] * N for _ in range(N)]
    # 현위치의 area를 반환
    cur_pos_by_area = defaultdict(set)
    for cr, cc in cur_pos:
        cur_pos_by_area[area_board[cr][cc]].add((cr,cc))

    for area in range(1, M+1):
        cur_path = path_by_area[area]
        if area in rot_cmd[turn]:
            r = rot_cmd[turn][area]
            if r != 0: # 시계, 반시계
                nxt_path = cur_path[-r:] + cur_path[:-r]
            else:
                nxt_path = cur_path
        else: nxt_path = cur_path

        # 0-1 보드 회전, cur_pos 재계산
        # 기존 cur_path의 위치에 nxt_path에 있던 값이 새롭게 온다.

        for i in range(len(cur_path)):
            cr, cc = cur_path[i]
            nr, nc = nxt_path[i]

            new_board[cr][cc] = zero_one_board[nr][nc]
            if area in cur_pos_by_area and (nr, nc) in cur_pos_by_area[area]:
                new_pos.append((cr, cc))

    zero_one_board = new_board
    return new_pos

def bfs(): # rotate함수가 생각보다 오래 걸렸고... bfs 순서를 잘못했어서 예제테케에서 좀 헤맨듯; 1:15:20
    cur_pos = [(M-1,M-1)]
    # for 최대 턴(T + 마름모 넓이 + 1?2?)
    for turn in range(1, max_turn):
        nxt_pos = []
        visited = set()

        # - 다음 []에 회전 적용된 좌표 리스트를 담음
        for cr, cc in cur_pos:
            cur_area = area_board[cr][cc]
            # - 이번 칸이 포탈일 경우
            # - 상하좌우, 다음 영역, 1임
            if zero_one_board[cr][cc] == -1:
                for d in [0,2,4,6]:
                    dr, dc = MOVE[d]
                    nr, nc = cr+dr, cc+dc
                    if 0<=nr<N and 0<=nc<N and not (nr,nc) in visited and cur_area+1 == area_board[nr][nc] and zero_one_board[nr][nc]!=0:
                        if area_board[nr][nc] == M and zero_one_board[nr][nc] == -1: return turn
                        visited.add((nr,nc))
                        nxt_pos.append((nr,nc))
            # - 이번 칸이 일반일 경우
            # - 대각선 인접, 동일 영역
            else:
                for d in [1,3,5,7]:
                    dr, dc = MOVE[d]
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < N and 0 <= nc < N and not (nr, nc) in visited and cur_area == area_board[nr][nc] and zero_one_board[nr][nc] != 0:
                        if area_board[nr][nc] == M and zero_one_board[nr][nc] == -1: return turn
                        visited.add((nr, nc))
                        nxt_pos.append((nr, nc))

        cur_pos = nxt_pos

        # - 이번 턴에서 회전이 있을 경우
        #     - cr, cc 재계산 (직접 계산)
        #     - 0-1 보드 회전 (직접 회전)
        if turn in rot_cmd:
            # pos 반환, path 수정, 0-1 보드 회전
            cur_pos = rotate(turn, cur_pos)

    return -1
def main():
    # ======================================
    # 0. 데이터 전처리
    # ======================================
    update_area_info() # 영역 정보 업데이트
    preprocess_rot_cmd() # 회전 명령 재구성
    can_exit = update_potal() # 탈출구 정보 업데이트 (탈출구/포털가 0 위치에 있으면 out)
    if not can_exit:
        print(-1)
        return
    # if DEBUG: print()
    # ======================================
    # 1. 이동 및 회전 진행
    # ======================================
    result = bfs()
    print(result)

main()