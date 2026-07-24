'''
십자 모양 폭발
https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-cross-shape-bomb
'''

MOVE = [(+1,0), (-1,0), (0,+1), (0,-1)]
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
tr, tc = map(int, input().split())

def remove_item():
    val = board[tr][tc]
    for i in range(val):
        for dr, dc in MOVE:
            nr, nc = dr*i+tr, dc*i+tc
            if 0<=nr<N and 0<=nc<N:
                board[nr][nc] = 0

def find_down_candidate(c):
    empty_end = -1
    down_candidate = []

    for r in range(N-1, -1, -1):
        if board[r][c] == 0 and empty_end == -1:
            empty_end = r
        elif board[r][c] > 0 and empty_end > -1:
            down_candidate.append(board[r][c])
            board[r][c] = 0

    return empty_end, down_candidate

def down_item(c, empty_end, down_candidate):
    r = empty_end
    for x in down_candidate:
        board[r][c] = x
        r -= 1

def main():
    remove_item()

    for c in range(N):
        # print()
        empty_end, down_candidate = find_down_candidate(c)
        # print(c, empty_end, down_candidate)
        # print(board)

        if empty_end > -1 and down_candidate:
            down_item(c, empty_end, down_candidate)
        # print(board)
    print('\n'.join([' '.join(map(str, board[i])) for i in range(N)]))

tr -= 1
tc -= 1
main()