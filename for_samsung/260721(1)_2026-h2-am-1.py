'''
아기 바다거북의 대모험: 해저 화산 지대:  2025 하반기 오전 1번 문제
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/a-little-sea-turtles-big-adventure/description

문제 분석: 38m 33s
코드 작성: 2h 53m 53s
디버깅: 5m 52s -> 100턴이 최대라는 점을 반영하지 않음(까먹음) -> 무한루프

총 소요 시간: 3h 38m 20s
'''
from collections import deque

N, M, K = 0, 0, 0
MOVE = [(0,1), (1,0), (0,-1), (-1,0)]

turtle_board = [[]] # 살아있는 거북이 실시간 좌표 (0 없음, 1 이상 거북이 번호)
item_board = [[]] # 산호초 -1, 화석 -2, 화산 번호(1~) 위치  (0 없음)
hot_board = [[]] # 현재 열기 (실시간 업데이트)
visited = [[]]

turtles = []
mountains = []
answer = []

live_turtles = set() # 맵 내에서 살아있는 거북이 (화석이 아니고, 탈출하지 않음)

class Turtle:
    # 거북이 상태 (상태(0생존, 1화석, 2탈출), 살아있을 경우 좌표)
    def __init__(self, num, r, c):
        self.status = 0
        self.num = num
        self.r = r
        self.c = c

class Mountain:
    # 화산 상태 (현재 압력, 임계치, 이번 턴 분출 여부)
    def __init__(self, max_p, r, c):
        self.cur_p = 0
        self.max_p = max_p
        self.r = r
        self.c = c
        # self.eruption = False

########################################################
###### 보조 함수
########################################################

#### 1. 값 입력
def input_data():
    global N, M, K, turtle_board, item_board, hot_board, turtles, mountains, visited, live_turtles, answer

    N, M, K = map(int, input().split())
    turtle_board = [ [0]*N for _ in range(N)]
    item_board = [ [0]*N for _ in range(N)]
    hot_board = [ [0]*N for _ in range(N)]
    visited = [ [False]*N for _ in range(N)]

    turtles = [None]*(M+1)
    mountains = [None]*(K+1)
    answer = [-1]*(M+1)

    live_turtles = {i for i in range(1, M+1)}

    # 바다 정보
    for i in range(N):
        # 0 빈공간, 1 산호초
        for j, v in enumerate(map(int, input().split())):
            if v == 1:
                item_board[i][j] = -1

    # 바다거북
    for num in range(1, M+1):
        r, c = map(int, input().split())
        turtle_board[r][c] = num
        turtles[num] = Turtle(num, r, c)

    # 화산
    for num in range(1, K+1):
        r, c, p = map(int, input().split())
        item_board[r][c] = num
        mountains[num] = Mountain(p, r, c)

# 최단경로 탐색 및 다음 좌표 반환
def bfs_turtle(sr, sc):

    def validation(r, c):
        # 방문 여부, 장애물, 범위 확인
        if (0<=r<N) and (0<=c<N) and (not visited[r][c]) and (turtle_board[r][c]==0) and (item_board[r][c] >= 0):
            return True
        return False

    # 방문 좌표 초기화
    for i in range(N):
        for j in range(N):
            visited[i][j] = False

    # 첫 출발 좌표 넣기
    q = deque([]) # 두번째 경로, 현재 위치
    for dr, dc in MOVE:
        nr, nc = sr+dr, sc+dc
        if validation(nr, nc):
            q.append( ( (nr, nc), (nr, nc) ) )
            visited[nr][nc] = True

    while q:
        (sec_r, sec_c), (cr, cc) = q.popleft()
        if cr == N - 1 and cc == N - 1:
            return cr, cc

        for dr, dc in MOVE:
            nr, nc = cr + dr, cc + dc
            if validation(nr, nc):
                if nr==N-1 and nc==N-1:
                    return sec_r, sec_c
                q.append( ( (sec_r, sec_c), (nr, nc) ) )
                visited[nr][nc] = True
    return -1, -1

# 거북이 이동 및 도착 여부 확인
def move_turtle(t, nr, nc, turn):
    if nr == -1 and nc == -1: return

    turtle_board[t.r][t.c] = 0
    t.r, t.c = nr, nc

    # 도착했을 경우 상태 업데이트
    if nr==N-1 and nc==N-1:
        t.status = 2
        live_turtles.remove(t.num)
        answer[t.num] = turn
        return

    turtle_board[nr][nc] = t.num

# 화산 압력 증가
def add_all_p():
    for num in range(1, K+1):
        mt = mountains[num]
        mt.cur_p += 10

# 연쇄 반응
def eruption():
    live_mountains = {i for i in range(1, K+1)} # 아직 분출하지 않은 화산 목록
    # print()
    # 루프 종료 조건
        # 1) 모든 화산이 분출됨
        # 2) 더 분출할 화산이 없음 (임계치 이상)
    while live_mountains:
        # 이번 반복에 분출이 하나라도 되었는지를 확인
        flag = False

        # 1. 열기 전파
        remove_mountains = set() # 이번 반복에서 제거되는 요소들
        for m_num in live_mountains:
            m = mountains[m_num]

            if m.cur_p + hot_board[m.r][m.c] < m.max_p : continue

            hot_board[m.r][m.c] += m.max_p
            for dr, dc in MOVE:
                nr, nc = m.r+dr, m.c+dc
                f = m.max_p // 2

                while 0<=nr<N and 0<=nc<N and item_board[nr][nc] != -1 and f > 0:
                    hot_board[nr][nc] += f
                    f //= 2
                    nr += dr
                    nc += dc

            remove_mountains.add(m_num)
            flag = True
            # print()
        live_mountains -= remove_mountains
        if not flag:
            break

    # 화석화
    for num in range(1, M+1):
        if num not in live_turtles: continue

        t = turtles[num]
        if hot_board[t.r][t.c] >= 20:
            t.status = 1
            turtle_board[t.r][t.c] = 0
            item_board[t.r][t.c] = -2
            live_turtles.remove(num)
    # print()
    # 분출하지 않은 화산을 반환
    return live_mountains

def reset_board(live_mountains):
    for i in range(N):
        for j in range(N):
            hot_board[i][j] = 0

    for num in range(1, K+1):
        if num in live_mountains: continue

        m = mountains[num]
        m.cur_p = 0

########################################################
###### 메인 함수
########################################################
def main():
    # 0단계: 데이터 입력
    input_data()
    # print()

    turn = 0
    while live_turtles and turn < 100:
        turn += 1
        #### 1단계: 바다거북 이동 ####
        # 1~M번 거북이 이동
        for m in range(1, M+1):
            if m not in live_turtles: continue

            # 1-1 최단 경로 탐색, 다음 좌표 반환
            t = turtles[m]
            nr, nc = bfs_turtle(t.r, t.c)
            # print()
            # 다음 좌표로 거북이 이동, 거북이 도착 시 상태 업데이트
            move_turtle(t, nr, nc, turn)
            # print()

        #### 2단계: 화산 압력 증가 ####
        add_all_p()

        #### 3단계: 화산 분출 및 연쇄 반응 ####
        live_mountains = eruption()
        # print()
        #### 4단계: 환경 초기화 ####
        reset_board(live_mountains)
        # print()

    # 정답 출력
    print('\n'.join(map(str, answer[1:])))

if __name__ == '__main__':
    main()