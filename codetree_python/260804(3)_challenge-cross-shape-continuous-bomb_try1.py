'''
십자 모양의 지속적 폭발
https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-cross-shape-continuous-bomb/description

'''

MOVE = [(0, 1), (0,-1), (1,0), (-1,0)]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cmds = [int(input())-1 for _ in range(M)]

def is_range(_r,_c):
    return 0<=_c<N and 0<=_r<N

def bomb(sr, sc):
    num = board[sr][sc]
    if num==0:
        return set()

    bomb_c = {sc}
    board[sr][sc] = 0

    for dr, dc in MOVE:
        nr, nc = sr+dr, sc+dc
        for n in range(num-1):
            if not is_range(nr, nc):
                break
            if board[nr][nc] > 0:
                board[nr][nc] = 0
                bomb_c.add(nc)

            nr += dr
            nc += dc

    return bomb_c

def find_target_r(tc):
    for _r in range(N):
        if board[_r][tc] > 0:
            return _r

    return -1

def gravity(bomb_c):
    for cc in bomb_c:
        tmp = []
        for cr in range(N):
            if board[cr][cc] > 0:
                tmp.append(board[cr][cc])
        for cr in range(N-1, -1, -1):
            if tmp:
                board[cr][cc] = tmp.pop()
            else:
                board[cr][cc] = 0


for c in cmds:
    # 폭탄 터뜨리고, 변화가 생기는 열 반환
    r = find_target_r(c)
    if r == -1: continue

    # 떨구기
    bomb_c_set = bomb(r, c)
    gravity(bomb_c_set)

print('\n'.join([' '.join(map(str, line)) for line in board]))

