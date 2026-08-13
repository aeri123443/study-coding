'''
왕실의 기사 대결: 2023 하반기 오전 1번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/royal-knight-duel/description

문제 분석: 10m 11s
코드 작성: 57m 14s
1차 디버깅: 8m 34s
  - [TC3 error] 처음에 moved_knights를 stack으로 구현하고 pop하면서 뒤에서부터 실제 이동을 적용시키려고 함 -> stack에 중복된 기사들이 담기면서 에러 발생
    -> moved_knights를 set으로 변경, 이에 따른 move_knight 함수 로직을 수정
2차 디버깅: 6m 27s
  - [TC5 fail] 수정 전에는 있었던 코드인데, 1차 디버깅으로 로직을 수정하면서 클래스의 sr, sc를 업데이트해주는 코드가 날아간 듯. 여기서 fail 발생
    -> 애초에 다른 테케를 어케 통과한건데?;;; 아무튼 바로 수정함

총 소요 시간: 1h 22m 26s
'''
from collections import deque

# ============================================
# 전역 선언 및 클래스
# ============================================

L, N, Q = -1, -1, -1
MOVE = [(-1,0), (0,+1), (+1,0), (0,-1)] # 위, 오른, 아래, 왼
board = []
knights = []
knights_board = []

class Knight:
    def __init__(self, num, r, c, h, w, k):
        self.num = num # 기사 번호
        self.sr = r
        self.sc = c
        self.h = h
        self.w = w
        self.k = k
        self.d = 0 # 대미지

# ============================================
# 보조 함수
# ============================================
# 초기 데이터 입력
def input_data():
    global L, N, Q, board, knights, knights_board

    L, N, Q = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(L)]
    knights_board = [[0]*L for _ in range(L)]
    knights = [0]*(N+1)

    # 기사 정보
    for num in range(1, N+1):
        r, c, h, w, k = map(int, input().split())
        sr, sc = r-1, c-1

        for r in range(sr, sr+h):
            for c in range(sc, sc+w):
                knights_board[r][c] = num

        new_knights = Knight(num, sr, sc, h, w, k)
        knights[num] = new_knights

# 기사 아웃 여부 판단
def is_out(kn):
    # 체력보다 받은 데미지의 양이 큼
    return kn.k <= kn.d

# 범위 여부 판단
def is_range(r, c):
    return 0<=r<L and 0<=c<L

# 이동 가능 여부(밀림 등) 판단
# 공격하는 기사 번호, 이동 방향
def can_move_simulation(a_num, d):
    dr, dc = MOVE[d]
    q = deque([a_num])
    moved_knights = {a_num}
    
    while q:
        k_num = q.popleft()
        kn = knights[k_num]
        sr, sc, h, w = kn.sr, kn.sc, kn.h, kn.w
        
        for r in range(sr, sr+h):
            for c in range(sc, sc+w):
                nr, nc = r+dr, c+dc
                # 이동 가능한지
                if is_range(nr, nc) and board[nr][nc] != 2:
                    # 해당 위치에 다른 기사가 있을 경우 큐에 담음
                    nxt_num = knights_board[nr][nc]
                    if nxt_num != 0 and nxt_num != k_num and not nxt_num in moved_knights:
                        q.append(nxt_num)
                        moved_knights.add(nxt_num)
                # 이동 불가할 경우 False와 빈 배열 반환
                else:
                    return False, []
    return True, moved_knights

# 기사 이동
# 이동하는 기사 스택, 공격 기사 번호, 방향
def move_knights(moved_knights, at_num, d):
    dr, dc = MOVE[d]

    # 기사들의 위치를 일괄 지움
    for num in moved_knights:
        kn = knights[num]
        sr, sc, h, w = kn.sr, kn.sc, kn.h, kn.w

        # 기존 위치를 지움!
        # 동시에 다음 위치에 대한 대미지도 누적 (아웃 여부 판정을 위함)
        for r in range(sr, sr + h):
            for c in range(sc, sc + w):
                knights_board[r][c] = 0

                # 다음 위치에 함정이 있을 경우, 대미지 누적
                nr, nc = r + dr, c + dc
                if num != at_num and board[nr][nc] == 1:
                    kn.d += 1

    # 새 위치 업데이트
    for num in moved_knights:
        kn = knights[num]

        if is_out(kn): continue

        sr, sc, h, w = kn.sr, kn.sc, kn.h, kn.w

        for r in range(sr, sr + h):
            for c in range(sc, sc + w):
                nr, nc = r+dr, c+dc
                knights_board[nr][nc] = num

        kn.sr += dr
        kn.sc += dc
# ============================================
# 메인 로직
# ============================================
def main():

    # 초기 데이터 입력
    input_data()
    # print()

    # 명령 수행
    for _ in range(Q):
        num, d = map(int, input().split())
        kn = knights[num]

        # 탈락한 기사는 명령 무시
        if is_out(kn): continue

        # 명령 받은 기사, 이동 가능한지 확인, 다른 기사들 있는지 반환
        # 다른 기사 있을 경우, 연쇄 밀림 후 밀림 가능 여부 반환
        can_move, moved_knights = can_move_simulation(num, d)

        # print()
        # 밀림 가능 시, 명령 받은 기사와 다른 모든 기사 이동, 대미지 누적
        if can_move:
            move_knights(moved_knights, num, d)

        # print()

    # 생존 기사의 대미지 검사
    total = 0
    for kn in knights[1:]:
        if is_out(kn): continue

        total += kn.d

    print(total)

main()