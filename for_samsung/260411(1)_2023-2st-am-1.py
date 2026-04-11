'''

왕실의 기사 대결: 2023 하반기 오전 1번 문제
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/royal-knight-duel/description

문제 분석: 19m 07s
코드 작성: 2h 01m 04s
디버깅: 45m 31s

총 소요 시간: 3h 05m 42s
'''
############################################
#### 전역 및 클래스 관리
############################################
L, N, Q = -1, -1, -1
MOVE = [(-1, 0), (0, +1), (+1, 0), (0, -1) ] # 위, 오른, 아래, 왼

class Knight:
    # 초기 체력, 누적 대미지, 현재r, 현재c, 너비, 높이
    def __init__(self, hp, damage, r, c, w, h):
        self.hp = hp
        self.damage = damage
        self.r = r
        self.c = c
        self.w = w
        self.h = h

        # 현재 위치 찾기
        pos = []
        for i in range(r, r+h):
            for j in range(c, c+w):
                pos.append( (i, j) )

        self.pos = pos


############################################
#### 함수 선언
############################################

# 보드판 입력
def input_board(board):
    for i in range(L):
        row = list(map(int, input().split()) )
        for j in range(L):
            board[i][j][0] = row[j]

# 기사 입력 및 배치
def input_knight(board, knights):
    for num in range(N):
        r, c, h, w, k = map(int, input().split())

        # 0 기준 좌표로 반환
        r -= 1
        c -= 1

        # 보드에 기사 위치 입력
        # 리팩토링: 클래스로 넣을 수 있는지 확인
        for i in range(r, r+h):
            for j in range(c, c+w):
                board[i][j][1] = num

        # 기사 정보 업데이트
        knights[num] = Knight(k, 0, r, c, w, h)

    return

# 기사 이동 가능 여부 확인(연쇄) -> 기사 현재 좌표 반환 (기사 num, [좌표 리스트])
def check_knights_movable(board, knights, num, d):
    movable_knights = []  # (기사 num, [좌표 리스트])
    movable_knight_set = set()
    di, dj = MOVE[d]
    is_movable = True

    def dfs(num):
        nonlocal is_movable

        # 한 기사의 각 좌표에 대하여
        for ci, cj in knights[num].pos:
            ni, nj = ci+di, cj+dj
            if 0<=ni<L and 0<=nj<L:
                # 다음 좌표가 벽이면 이동 불가
                if board[ni][nj][0] == 2:
                    is_movable = False
                    return False
                # 다음 좌표에 ''다른'' 기사가 있으면
                # 그 기사''들''에 대해 dfs 수행
                elif board[ni][nj][1] >= 0 and board[ni][nj][1] != num:
                    if board[ni][nj][1] not in movable_knight_set:
                        movable_knights.append( board[ni][nj][1] )
                        movable_knight_set.add( board[ni][nj][1] )
                        result = dfs( board[ni][nj][1] )
                        if not result: return False
            # 다음 좌표가 바깥이면 이동 불가
            else:
                is_movable = False
                return False

        return is_movable

    dfs(num)

    # if is_movable: return movable_knights
    # else: return {}
    return (is_movable, movable_knights)

def move_knights(board, knights, num, movable_knights, d):
    di, dj = MOVE[d]
    damaged_knight = set() # 피해 입은 기사 정보를 저장

    # 명령 외 기사 이동 (역순!)

    # 기사 싹 지우고, 새 위치를 클래스에 업데이트
    for mk in movable_knights[::-1]:
        pos = knights[mk].pos
        new_pos = []

        for ci, cj in pos:
            board[ci][cj][1] = -1  # 기존 좌표를 지우고
            new_pos.append((ci + di, cj + dj))  # pos 업데이트

        # 새 좌표를 보드에 배치
        knights[mk].pos = new_pos
        knights[mk].r += di
        knights[mk].c += dj
        # for ni, nj in new_pos:
        #     board[ni][nj][1] = mk
        #     # 해당 위치에 장애물이 있으면, 피해 적용
        #     if board[ni][nj][0] == 1:
        #         knights[mk].damage += 1
        #         damaged_knight.add(mk)

    # 기사 싹 배치
    for mk in movable_knights[::-1]:
        new_pos = knights[mk].pos
        for ni, nj in new_pos:
            board[ni][nj][1] = mk
            # 해당 위치에 장애물이 있으면, 피해 적용
            if board[ni][nj][0] == 1:
                knights[mk].damage += 1
                damaged_knight.add(mk)

    # 명령 받은 기사 이동
    # 리팩토링
    pos = knights[num].pos
    new_pos = []

    for ci, cj in pos:
        board[ci][cj][1] = -1 # 기존 좌표를 지우고
        new_pos.append( (ci+di, cj+dj) ) # pos 업데이트

    # 새 좌표를 보드에 배치
    knights[num].pos = new_pos
    knights[num].r += di
    knights[num].c += dj
    for ni, nj in new_pos:
        board[ni][nj][1] = num

    return damaged_knight

def cal_score(knights):
    score = 0

    for knight in knights.values():
        if knight.hp > knight.damage:
            score += knight.damage

    return score

# 기사 제거
def remove_knight(board, knights, num):
    pos = knights[num].pos

    for i, j in pos:
        board[i][j][1] = -1

    del knights[num]
############################################
#### 메인 로직
############################################

def main():
    global L, N, Q

    L, N, Q = map(int, input().split())
    board = [ [ [-1, -1] for _ in range(L) ] for _ in range(L)] # [ 빈칸0/함정1/벽2, 기사 num (0 ~ N-1 치환) ]
    knights = {} # {num: Knight Class}

    # 입력 및 배치
    input_board(board)
    input_knight(board, knights)

    # 명령 수행
    for _ in range(Q):
        num, d = map(int, input().split())
        num -= 1 # 0 기준으로 변환

        # 사라진 기사면 넘어감
        # if knights[num].hp <= knights[num].damage:
        if num not in knights:
            continue

        # 기사 이동 가능 여부 확인(연쇄) -> 기사 현재 좌표 반환 (기사 num, [좌표 리스트])
        (is_movable, movable_knights) = check_knights_movable(board, knights, num, d)

        # 이동 가능할 경우, 이동 수행 후 피해 정보 반환
        if not is_movable:
            continue

        damage_knights = move_knights(board, knights, num, movable_knights, d)

        # out 기사 확인
        if damage_knights:
            for dk in damage_knights:
                if knights[dk].hp <= knights[dk].damage:
                    remove_knight(board, knights, dk)
                    # del knights[dk]
        # print()
    # 생존 기사의 피해량 합산
    score = cal_score(knights)
    print(score)

if __name__ == '__main__':
    main()