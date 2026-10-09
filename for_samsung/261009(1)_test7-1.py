# 1회독 6:05
# 2회독 7:35
# 설계 빛방향 38:44 + bfs 10:21
# 전역 중 상태 변하는 건 딱히 없음
from collections import deque
import tracemalloc
tracemalloc.start()
N, M, K = map(int, input().split())

# 보드
item_board = [list(input()) for _ in range(N)] # 양수: 등대 번호, 음수: 암초 번호, 0: 빈 공간
lights_board = [[] for _ in range(4)]# - 빛 맵[0~4] = [맵 모양 board] 빛 있T/없F

# 방향 정보
MOVE = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,+1)]
LIGHTS = [ [(i-1)%8, i, (i+1)%8] for i in range(8)]

# 클래스 관리

lamps = [None] # 등대들. [num] 등대
stones = [None] # 암초들. [num] (r,c)

# 등대
class Lamp:
    def __init__(self, num, r, c, d_list):
        self.num = num
        self.pos = (r,c)
        self.d_list = d_list # 방향 순서

# 전역 작성 13:40


# 등대, 암초 위치 정보 업데이트
def update_item_pos(): # 8:46
    global item_board

    b = [[0]*M for _ in range(N)]

    # 암초, 보드 업데이트
    for r in range(N):
        for c in range(M):
            if item_board[r][c] == '#':
                b[r][c] = -len(stones)
                stones.append((r,c))
    # 등대, 보드 업데이트
    for i in range(1, K+1):
        r, c, *d_list = map(int, input().split())
        r, c = r-1, c-1
        b[r][c] = i
        lamps.append(Lamp(i, r, c, d_list))

    item_board = b

# 특정 방향으로 라인 하나 긋고, 만나는 등대/암초 반환
# sr, sc: 시작 위(얘도 포함)
# d 라인 그릴 방향, num 기록할 숫자(0 빈 공간. 1 빛, 2 가려짐)
def draw_line(board, sr, sc, d, num): # 작성 및 방향 테케 생성 14:57
    met_items = set()
    dr, dc = MOVE[d]
    cr, cc = sr, sc

    while 0<=cr<N and 0<=cc<M:
        board[cr][cc] = num

        # 다른 아이템 만나면 기록
        if item_board[cr][cc] != 0:
            met_items.add(item_board[cr][cc])

        cr+=dr
        cc+=dc

    return met_items

# 특정 방향의 범위 그리기 (r, c, d)
# look_d: 등대/암초가 보는 방향
# num: 보드에 기록할 숫자 (0/1/2)
def draw_d_area(board, sr, sc, look_d, draw_d, num):  # 12:49 + 12:41
    met_items = set()

    d = LIGHTS[look_d][draw_d]
    dr, dc = MOVE[d]
    cr, cc = sr+dr, sc+dc

    # 특정 방향으로 시작점 이동
    while 0<=cr<N and 0<=cc<M:
        # 직선(LIGHT[d][1]) 방향으로 라인 긋기, 만난 등대/암초들 누적 및 일괄 반환
        met = draw_line(board, cr, cc, LIGHTS[look_d][1], num)
        if met: met_items.update(met)

        cr+=dr
        cc+=dc

    return met_items

# 특정 초 특정 등대의 빛 방향
# look_d: 등대/암초가 보는 방향
def get_item_map_by_turn_and_lamp(l_num, turn): # 39:19
    board = [[0]*M for _ in range(N)]
    l = lamps[l_num]
    look_d = l.d_list[turn%4]
    sr, sc = l.pos

    # 등대 기본 방향 기록
    for draw_d in range(3):
        if draw_d == 0: m_draw_d_list = [0,1]
        elif draw_d == 1: m_draw_d_list = [1]
        else: m_draw_d_list = [1,2] # 3

        # 다른 등대 만나면, 가려지는 함수로 표시
        hidden = set()
        new_met = draw_d_area(board, sr, sc, look_d, draw_d, 1)
        for m_num in new_met:
            if m_num in hidden: continue
            mr, mc = lamps[m_num].pos if m_num > 0 else stones[-m_num]
            for m_draw_d in m_draw_d_list:
                new_hidden = draw_d_area(board, mr, mc, look_d, m_draw_d, 2)
                if new_hidden: hidden.update(new_hidden)
    return board

def get_light_map_by_turn(turn): # 10:25
    # 초 board 생성
    turn_board = [[False]*M for _ in range(N)]

    # def 특정 초 특정 등대의 빛 방향
    for l_num in range(1, K+1):
        lamp_board = get_item_map_by_turn_and_lamp(l_num, turn)
        # 초 board에 업데이트 (빛 받는 부분만)
        for r in range(N):
            for c in range(M):
                if lamp_board[r][c] == 1 and not turn_board[r][c]:
                    turn_board[r][c] = True

    # 초 board 등록
    lights_board[turn%4] = turn_board


# ** 멈춰있을 때 반영하기
def bfs(): #13:59
    # visited[r][c][turn%4] = T/F
    visited = [[[False]*4 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = True
    # 큐 (위치, 턴)
    q = deque([(0,0,0)])

    def append_q(r, c, t):
        q.append((r, c, t))
        visited[r][c][t%4] = True

        # print(f' next: pos {r},{c}')

    def check_light(r,c,t):
        return lights_board[t%4][r][c]

    while q:
        cr, cc, turn = q.popleft()
        # print()
        # print(f'cur: turn {turn}, pos {cr},{cc}')

        # 가만히 있는 선택지
        if not visited[cr][cc][(turn+1)%4]:
            append_q(cr, cc, turn+1)

        # - 이번 턴 빛 있음 -> 4방향&가만히있는거 이동 시도
        # - 이번 턴 빛 없음 -> 가만히 있는 것만
        if not check_light(cr,cc,turn): continue

        for d in [0,2,4,6]:
            dr, dc = MOVE[d]
            nr, nc = cr+dr, cc+dc

            # - 격자 내, 턴방향 기준 방문여부, 등대/암초 없음
            if 0<=nr<N and 0<=nc<M and not visited[nr][nc][(turn+1)%4] and item_board[nr][nc] == 0:
                # 빛 이번좌표 다음좌표 둘다 있어야 함
                if check_light(nr,nc,turn):
                    # 이동 가능하고 도착임 -> return
                    if (nr,nc) == (N-1, M-1):
                        return turn+1
                    append_q(nr,nc,turn+1)
    # print()
    return -1

def main():
    # 등대, 암초 위치 정보 업데이트
    update_item_pos()

    # 빛 방향 정보 업데이트
    for t in range(4):
        get_light_map_by_turn(t)

    # dk아 당떨어져... 시야각해봐서 ㄱㅊ을줄알앗는데 여전히오래걸리네 당떨어져서 초콜릿먹고온시간 1:45

    cnt = bfs()
    print(cnt)

main()

# 설계 읽으면서 빼먹은 부분 있나 확인 1:5
# fail 디버깅: bfs 다음 큐 넣는 과정에서, 습관적으로 0<=nc<N ㅇㅈㄹ. ,. ,. 예외케이스 있는줄알고 틀린 테케 다시 그려보고 디버깅해봤더니 끝값이 안 보이길래 엥설마?하고 보니 ...
    # 하..암튼 13:43
# 엥? 메모리초과 ㅇㅈㄹ 기껏 시간복잡도 계산햇더만 내가 공간복잡도까지 고려해야햇다코 일단 패~스
c, p = tracemalloc.get_traced_memory()
print()
print(c/1024/1024, p/1024/1024)