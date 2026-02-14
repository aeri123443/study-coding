'''
17679. Lv.2 [1차] 프렌즈4블록
https://school.programmers.co.kr/learn/courses/30/lessons/17679
'''
from collections import deque
from pprint import pprint

M, N = 0, 0
game_board = [] # 비어있는 곳 == 0, find_group에서 임시방문처리==소문자 (지울 녀석 기록용)
# visited = []
move = [(0,1), (1,0), (1,1)]

# 방문 가능 좌표 확인
def can_move(i, j):
    # 범위 내 & 비어있지 않음
    if 0<=i<M and 0<=j<N and game_board[i][j]!=0:
        return True

    return False

# 그룹 찾고
def find_group(si, sj, sc):
    # print(si, sj, sc)

    # 2*2 범위 모두 진입가능한지 & 동일 문자인지 확인?
    can_next = True
    for di, dj in move:
        ni, nj = si+di, sj+dj
        if not can_move(ni, nj):
            # print(ni, nj, "can not move")
            can_next = False
            break
        if not (str.upper(game_board[ni][nj])==sc):
            # print(ni, nj, "not same")
            can_next = False
            break

    if can_next:
        game_board[si][sj] = str.lower(game_board[si][sj])
        # print(si, sj, 'can_next')
        for di, dj in move:
            ni, nj = si+di, sj+dj
            if game_board[ni][nj].islower(): continue
            game_board[ni][nj] = str.lower(game_board[ni][nj])
            find_group(ni, nj, sc)
# 지우고 아래로
def remove_and_down():
    updated = 0
    for j in range(N):
        last_null = deque()
        for i in range(M-1, -1, -1):
            if game_board[i][j] == 0:
                continue
            
            # 소문자: 제거 대상
            if game_board[i][j].islower():
                game_board[i][j] = 0
                last_null.append(i)
                updated += 1
            # 대문자: 하강 후보
            elif last_null:
                game_board[last_null.popleft()][j] = game_board[i][j]
                game_board[i][j] = 0
                last_null.append(i)
    return updated

def solution(m, n, board):
    global M, N, game_board

    M, N = m, n
    game_board = [list(arr) for arr in board]
    answer = 0
    # visited = [[False]*N for _ in range(N)]
    # pprint(game_board)

    # 업데이트가 없을 때까지 반복
    while True:
        # 그룹 찾기
        for i in range(M):
            for j in range(N):
                if can_move(i, j):
                    find_group(i, j, game_board[i][j])
        # pprint(game_board)

        # 지우고 넣기
        updated = remove_and_down()
        if not updated:
            break
        # print(updated)
        # pprint(game_board)
        answer += updated

    return answer

print()
print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(14)

print()
print(solution(6,6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
print(15)
