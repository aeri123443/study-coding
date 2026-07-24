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

def set_gravity():
    for c in range(N):
        tmp = [board[r][c] for r in range(N-1, -1, -1) if board[r][c]>0]
        # print(tmp)
        tmp_len = len(tmp)
        tmp_idx = 0
        for r in range(N-1, -1, -1):
            if tmp_idx < tmp_len:
                board[r][c] = tmp[tmp_idx]
                tmp_idx+=1
            else:
                board[r][c] = 0

        # print(board)
def main():
    remove_item()
    # print(board)
    set_gravity()
    print('\n'.join([' '.join(map(str, board[i])) for i in range(N)]))

tr -= 1
tc -= 1
main()