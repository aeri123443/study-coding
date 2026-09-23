'''
방향에 맞춰 최대로 움직이기
https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-max-movements-with-direction/description

문제 분석: 6m 35s
코드 작성: 16m 27s
최종 디버깅: 0m 0s

총 소요 시간: 23m 2s
'''

MOVE = [
    (),
    (-1,0), (-1,1), (0,1), (1,1),
    (1,0), (1,-1),(0,-1), (-1,-1)
    ]
N = int(input())
num_board = [list(map(int, input().split())) for _ in range(N)]
dir_board = [list(map(int, input().split())) for _ in range(N)]
sr, sc = map(lambda x: int(x)-1, input().split())

answer = 0
def dfs(cr, cc, cnt):
    global answer
    answer = max(answer, cnt)

    c_num = num_board[cr][cc]

    dr, dc = MOVE[dir_board[cr][cc]]
    nr, nc = cr+dr, cc+dc
    while 0<=nr<N and 0<=nc<N:
        if c_num < num_board[nr][nc]:
            dfs(nr, nc, cnt+1)
        else:
            answer = max(answer, cnt)
        nr, nc = nr+dr, nc+dc

dfs(sr, sc, 0)
print(answer)