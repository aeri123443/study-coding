'''
마법의 숲 탐색: 2024 상반기 오후 1번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/magical-forest-exploration/description

문제 분석: 20m 38s
코드 1차 작성: 1h 20m 31s
  - [TC3 Fail] 숲의 범위 확인 단계에서, 골렘 중심좌표에서 상하좌우를 살폈어야 했는데, 중심좌표만 검사하면서 오답 발생
코드 1차 디버깅 + 2차 작성: 12m 31s
  - [TC34 Fail] r,c의 (중심)위치만 생각했는지 r 패딩을 2개만 넣었었는데, 골렘 크기 생각해서 3개로 확장했어야 했다. is_range(r, c, Ture)에서 걸림.
코드 2차 디버깅 + 3차 작성: 42m 03s

총 소요 시간: 2h 35m 50s
'''

from collections import deque

########################################################################
#### 전역 변수 및 클래스
########################################################################
N, M, K = -1, -1, -1
MOVE = [(-1, 0), (0, +1), (+1, 0), (0, -1)]  # 북동남서
CHECK = [  # 이동 우선순위: 남 - 서남 - 동남
    ((+1, -1), (2, 0), (+1, +1)),  # 남
    ((-1, -1), (0, -2), (+1, -2), (+1, -1), (+2, -1)),  # 서 - 남
    ((-1, +1), (0, +2), (+1, +1), (+1, +2), (+2, +1))  # 동 - 남
]

board = []
golems = {}


class Golem:
    def __init__(self, r, c, d):
        self.r = r
        self.c = c
        self.d = d


########################################################################
#### 보조 함수
########################################################################
## 초기 데이터 입력 및 생성
def input_data():
    global N, M, K, board, golems

    N, M, K = map(int, input().split())

    # r은 위로 세 칸 더 만듦
    board = [[-1] * M for _ in range(N + 3)]


## 범위 확인
# Padding: T(위의 2개 패딩 적용했을 때), F(적용하지 않았을 때-r 2 이상, default)
def is_range(r, c, padding=False):
    if padding:
        return 0 <= r < N + 3 and 0 <= c < M
    else:
        return 3 <= r < N + 3 and 0 <= c < M


## 골렘 회전 방향 반환
def rotate_golem(cd, md):
    # 남쪽: 그대로
    if md == 0:
        return cd
    # 서남: 반시계
    elif md == 1:
        return (cd - 1) % 4
    # 남서: 시계
    elif md == 2:
        return (cd + 1) % 4
    return -1


## 이동 우선순위 반환
def check_move_d(c, d):
    cc, cd = c, d
    cr = 0  # 초기 위치

    while True:

        moved = False

        for i, check_d in enumerate(CHECK):

            # 범위 내, 다른 골렘 없음
            # print(all([is_range(cr+dr, cc+dc, True) and board[cr+dr][cc+dc]==-1 for dr, dc in check_d]))
            # print()
            if all([is_range(cr + dr, cc + dc, True) and board[cr + dr][cc + dc] == -1 for dr, dc in check_d]):
                # 골렘 중심 위치 및 방향 업데이트
                if i == 0:  # 남쪽
                    cr += 1
                elif i == 1:  # 서남: 반시계
                    cr += 1
                    cc -= 1
                    cd = (cd - 1) % 4
                else:  # 동남: 시계
                    cr += 1
                    cc += 1
                    cd = (cd + 1) % 4

                moved = True
                break

        if not moved:
            return cr, cc, cd


## 요정 이동
## 중앙 시작 - board 골렘 번호와 방향 확인하며 내려감
def bfs(sr, sc):
    q = deque([(sr, sc)])
    visited = [[False] * M for _ in range(N + 3)]
    visited[sr][sc] = True
    max_r = sr

    while q:
        cr, cc = q.popleft()
        g_num = board[cr][cc]

        for dr, dc in MOVE:
            nr, nc = cr + dr, cc + dc

            if is_range(nr, nc) and not visited[nr][nc] and board[nr][nc] > -1:
                # 다음 좌표가 같은 골렘이면 문제 없음
                # 다음 좌표가 다른 골렘이면, 이번 좌표가 출구여야 함
                if g_num != board[nr][nc]:
                    # 이번 골렘의 출구는?
                    g = golems[g_num]
                    ex_d = g.d
                    e_dr, e_dc = MOVE[ex_d]
                    e_r, e_c = g.r + e_dr, g.c + e_dc

                    if (cr, cc) != (e_r, e_c):
                        continue

                visited[nr][nc] = True
                q.append((nr, nc))
                max_r = max(max_r, nr)
    # print()
    return max_r


########################################################################
#### 메인 로직
########################################################################
def main():
    global board, golems

    ### 0단계: 초기 데이터 입력 및 생성
    input_data()
    answer = []  # 디버깅을 위해 하나씩 담은 후 마지막에 합침

    for k in range(K):
        ### 1단계: 골렘 이동 (r, c 수정하기)

        ## 값 입력
        c, d = map(int, input().split())
        c -= 1  # 0-index로

        ## 이동 우선순위 반환
        r, c, d = check_move_d(c, d)
        # print()
        ## 숲 범위 확인, 범위 밖이면 초기화
        if not all([is_range(r + dr, c + dc) for dr, dc in MOVE + [(0, 0)]]):
            answer.append(0)

            board = [[-1] * M for _ in range(N + 3)]
            golems = {}

            continue

        ## 실제 이동
        golems[k] = Golem(r, c, d)
        board[r][c] = k
        for dr, dc in MOVE: board[r + dr][c + dc] = k

        # print()

        ### 2단계: 정령 이동
        ## 중앙 시작 - board 골렘 번호와 방향 확인하며 내려감
        max_r = bfs(r, c)

        ### 3단계: 최종 r 위치 저장 (r 수정하기)
        answer.append(max_r - 2)
        # print()
    print(sum(answer))

main()