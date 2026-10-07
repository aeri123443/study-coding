"""
생각
    - '턴이 지나고 나서의 보드의 상태'를 미리 저장하는 선택지
    - 회전명령 200회, M 50 -> 가능
    - i 포털 근처에서 왔다갔다만 하다가 회전으로 i+1 영역 포털에 가까워지자마자 이도하는게 최소 턴수일 가능성이 있을까?
        - 그러면 전체 bfs 말고, 각 턴에따라 i 포탈 -> i+i 포탈 최대한 빠르게 가는 bfs를 각자 구하는건? -> 이렇게 해보면 될듯
        - 특정 칸에 머무르는 건 불가하다고 햇으니, 구태여 왔다갔다하는 케이스도 은연중에 뺀듯!!
        - 그러면 처음 계획했던대로 보드 상태 저장하고, bfs마다 턴(이동횟수)에 따른 위치랑 탈출구 등을 보정하자.
" 각 칸이 처음 위치 기준 어디에 해당하는지 를 기록 "
    -
N*N 내부의 M 게임판(마름모)
M = (N+1)/2
MOVE 8방향
말 위치 '초기 보드' 기준
영역 보드 - 1, 2, M ... 영역 표시
초기 보드 - 0, 1 정보
초기 -> 현재 [t] {매핑} t턴, {초기 (r,c) : 현재(r,c)}
현재 -> 초기 [t] {매핑}

회전 명령 {턴수: {x: r}} - 반시계, + 시계

게임판
    - 중앙 1번에서 출발
    -
    - 포탈: 각 영역마다 존재,
    - 장애물: 말 이동 가능 1, 불가능 0

def 회전 명령 전처리():
    - 회전 명령 훑다가, 새로운 턴이 나오면, 그 전 턴까지의 상태를 일괄 업데이트
        -
    - +, - 해가며 최종 명령 결과 반환
    - 해당 턴의 명령을 전역변수로 업데이트
    - 어차피 누적되니 모든 턴을 기록
    - 마지막 턴 따로 기록하기

def 회전 상태 저장:
    - 회전 명령 기준
        - 턴마다 회전 진행
        - 회전 결과를 매핑에 저장
* 회전 규칙
    - 턴에서 말이 이동한 다음임
    - t, x, d, r
    - t턴에 x 영역이 d방향으로 r만큼 회전
    - 턴에 회전이 두군데 일어날 수 있음, 시간순서대로 주어짐
    - 반시계 -1, 시계 -1
    - 게임 말, 포탈, 탈출구 회전

def bfs():
    1. 말의 이동
        - 공통 규칙
            - 모든 기록의 기준은 초기 보드 기준
            - 현위치는 현재 턴에 따른 보드판을 사용
            - 다음 위치는 다음 위치에 따른 보드판을 사용
            - 이번 턴(현재 cnt)에서 회전이 일어났을 경우, 회전 명령에 따라 다음 턴을 보정하여 말의 위치를 push
        1) 현위치가 포탈이 아닐 경우
            - 이동: 대각선으로 인접, 영역이 같은 칸
            - 초기 보드 기준으로 이동
        2) 현위치가 포탈일 경우
            - 이동: 상하좌우 인접, 다음 영역(i -> i+1)으로 이동
            - 초기위치가 지금 보드 어디에 있는지 매핑
            - 상하좌우로 지금 보드 기준 갈 수 있는곳 찾음
            - 다시 초기위치로 변환후 visited, q 업데이트
    2.
for 턴
    1. 말의 이동
    2. 회전


# 1회독, 예제 이해 10m 16
# 2회독 8m 27s
# 설계 57m 21s
# 상태... 크게 변화하는게 전역 중에는 없는듯... 2m 20s
5 2

0 0 0 0 0
0 0 0 1 0
1 1 1 0 1
0 1 1 1 0
0 0 1 0 0

3 3
4 3
3 1

1 2 1 2
1 3 -1 3

"""

# 1회독, 예제 이해 10m 16
# 2회독 8m 27s
# 설계 57m 21s
# 상태... 크게 변화하는게 전역 중에는 없는듯... 2m 20s

# 케이스 확인: 이동 불가할 경우

"""" 각 칸이 처음 위치 기준 어디에 해당하는지 를 기록 """

from collections import deque, defaultdict

DEBUG = True
N, T = map(int, input().split())
M = (N+1)//2
MOVE = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)] # 시계방향 기준

R, C = N//2, N//2 # 말 위치 '초기 보드' 기준

cmd_turn = []
# 영역 보드 - 1, 2, M ... 영역 표시
area_board = [[0]*N for _ in range(N)]
# 초기 보드 - 0, 1 정보, 포탈은 -1
initial_board = [list(map(int,input().split())) for _ in range(N)]
# 초기 -> 현재 [t] {매핑} t턴, {초기 (r,c) : 현재(r,c)}
init_to_cur = []
# 현재 -> 초기 [t] {매핑}
cur_to_init = []

# 회전 명령 {턴수: {x: r}} - 반시계, + 시계
rot_cmd = {}

# 전역 작성까지 10m 26s

def update_area():
    area_board[R][C] = 1
    stack = [(R,C)]
    for num in range(2, M+1):
        new_stack = []
        for r, c in stack:
            for d in [0, 2, 4, 6]:
                dr, dc = MOVE[d]
                nr, nc = r + dr, c + dc
                if 0<=nr<N and 0<=nc<N and area_board[nr][nc]==0:
                    new_stack.append((nr,nc))
                    area_board[nr][nc] = num
        stack = new_stack

# 회전 명령 전처리
# +, - 해가며 최종 명령 결과 반환
# 해당 턴의 명령을 전역변수로 업데이트
# 어차피 누적되니 모든 턴을 기록
def preprocess_rot():
    global cmd_turn

    # 회전 명령 훑다가,
    # 회전 명령 {턴수: {x: r}} - 반시계, + 시계
    # rot_cmd = {}
    prev_rot_turn = 0
    rot = defaultdict(int)
    for  _ in range(T):
        t, x, d, r = map(int, input().split())

        # 새로운 턴이 나오면, 그 전 턴까지의 상태를 일괄 업데이트
        if prev_rot_turn != t:
            rot_cmd[prev_rot_turn] = {k: v for k, v in rot.items()}
            cmd_turn.append(prev_rot_turn)
            prev_rot_turn = t

        rot[x] += (d*r)

    # 마지막 턴 따로 기록하기
    rot_cmd[prev_rot_turn] = {k: v for k, v in rot.items()}
    cmd_turn.append(prev_rot_turn)


def init_data(): # 1h 44m 57s
    global init_to_cur, cur_to_init
    # area_board 업데이트
    update_area()

    # 포탈 정보 업데이트
    # 포탈이 0 위치에 있을 경우, 이동 불가로 판정
    for _ in range(M):
        r, c = map(lambda x: int(x)-1, input().split())
        if initial_board[r][c] == 0: return False
        initial_board[r][c] = -1

    # 회전 명령 전처리
    preprocess_rot()

    # 영역별 path 반환
    # 아니 이거 먼저 만들고 area board 업뎃할걸
    path_by_area = [[], [(R, C)]]
    for m in range(1,M):
        path = []
        cr, cc = R-m, C
        for d in [3, 5, 7, 1]:
            dr, dc = MOVE[d]
            for _ in range(m):
                path.append((cr,cc))
                cr+=dr
                cc+=dc
        path_by_area.append(path)

    init_to_cur = {}
    cur_to_init = {}
    for turn in cmd_turn:
        if turn not in rot_cmd: continue
        if turn == 0: continue
        init_to_cur[turn] = {}
        cur_to_init[turn] = {}
        for m, r in rot_cmd[turn].items():
            path = path_by_area[m]
            # 시계방향(r > 0), 반시계방향(r<0)모두 동일
            cur_path = path[r:] + path[:r]
            for idx in range(len(cur_path)):
                ir, ic = path[idx]
                cr, cc = cur_path[idx]
                init_to_cur[turn][(ir,ic)] = (cr,cc)
                cur_to_init[turn][(cr,cc)] = (ir,ic)

    # 나머지 값 업데이트
    init_to_cur[0] = {(r,c):(r,c) for r in range(N) for c in range(N)}
    cur_to_init[0] = {(r,c):(r,c) for r in range(N) for c in range(N)}

    max_t = max(rot_cmd.keys())
    for turn in range(1, max_t+1):
        if turn not in init_to_cur:
            init_to_cur[turn] = {(a,b): (c,d) for (a,b), (c,d) in init_to_cur[turn-1].items()}
            cur_to_init[turn] = {(a,b): (c,d) for (a,b), (c,d) in cur_to_init[turn-1].items()}
        else:
            for (a,b), (c,d) in init_to_cur[turn-1].items():
                if (a,b) not in init_to_cur[turn]:
                    init_to_cur[turn][(a,b)] = (c,d)
                    cur_to_init[turn][(c,d)] = (a,b)

    return True

# 1. 말의 이동
#     - 공통 규칙
#         - 모든 기록의 기준은 초기 보드 기준
#         - 현위치는 현재 턴에 따른 보드판을 사용
#         - 다음 위치는 다음 위치에 따른 보드판을 사용
#         - 이번 턴(현재 cnt)에서 회전이 일어났을 경우, 회전 명령에 따라 다음 턴을 보정하여 말의 위치를 push
#         - 매 이동에서 초기위치 -> 현재 위치, 현재 위치 -> 초기 위치 변환
def bfs():
    q = deque([(R, C)])
    visited = [ [-1]*N for _ in range(N)]
    visited[R][C] = 0

    while q:
        cr, cc = q.popleft()
        cur_area = area_board[cr][cc]
        cnt = visited[cr][cc]

        # 1) 현위치가 포탈이 아닐 경우
        if initial_board[cr][cc] != -1:
            for d in [1,3,5,7]:
                dr, dc = MOVE[d]
                nr, nc = cr+dr, cc+dc
                # 이동: 대각선으로 인접, 영역이 같은 칸
                if 0<=nr<N and 0<=nc<N and visited[nr][nc] == -1 and area_board[nr][nc] == cur_area and initial_board[nr][nc] != 0:
                    q.append((nr,nc))
                    visited[nr][nc] = cnt+1
                # print()

        # 2) 현위치가 포탈일 경우
        else:
            # - 마지막 영역이면 반환!
            if cur_area == M:
                return cnt
            else:
                # 현재턴의 진짜 위치
                cur_cr, cur_cc = init_to_cur[cnt][(cr,cc)]

                # 이동: 상하좌우 인접, 다음 영역(i -> i+1)으로 이동
                for d in [0,2,4,6]:
                    dr, dc = MOVE[d]
                    cur_nr, cur_nc = cur_cr+dr, cur_cc+dc
                    init_nr, init_nc = cur_to_init[cnt][(cur_nr, cur_nc)]

                    if 0<=cur_nr<N and 0<=cur_nc<N and visited[init_nr][init_nc] == -1 and area_board[cur_nr][cur_nc] == cur_area+1:
                        if initial_board[init_nr][init_nc] != 0:
                            q.append((init_nr, init_nc))
                            visited[init_nr][init_nc] = cnt + 1
                    # print()
    # print()
    return -1

def main():
    if not init_data():
        print(-1)
        return

    print(bfs())

main()