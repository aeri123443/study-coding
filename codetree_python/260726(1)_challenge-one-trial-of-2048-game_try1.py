'''
단 한 번의 2048 시도
https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-one-trial-of-2048-game/description

문제 분석: 3m 14s
코드 작성: 26m 33s
최종 디버깅: 0m 0s
-> 함수화하면 더 편했을듯!

총 소요 시간: 29m 47s
'''

N = 4
MOVE = {
    'L': (0, -1),
    'R': (0, +1),
    'U': (-1, 0),
    'D': (+1, 0)
}
board = [list(map(int, input().split())) for _ in range(N)]
nxt_board = [[0]*N for _ in range(N)]
# print()

d = input()

if d == 'L':
    for r in range(N):
        stack = []
        for c in range(N):
            num = board[r][c]
            if num == 0: continue

            if stack and stack[-1][0] == num and stack[-1][1] == False:
                stack[-1] = [num*2, True]
            else:
                stack.append([num, False])

        for c, x in enumerate(stack):
            nxt_board[r][c] = x[0]
elif d == 'R':
    for r in range(N):
        stack = []
        for c in range(N-1, -1, -1):
            num = board[r][c]
            if num == 0: continue

            if stack and stack[-1][0] == num and stack[-1][1] == False:
                stack[-1] = [num*2, True]
            else:
                stack.append([num, False])

        for c, x in enumerate(stack):
            nxt_board[r][N-c-1] = x[0]
elif d == 'U':
    for c in range(N):
        stack = []
        for r in range(N):
            num = board[r][c]
            if num == 0: continue

            if stack and stack[-1][0] == num and stack[-1][1] == False:
                stack[-1] = [num * 2, True]
            else:
                stack.append([num, False])

        for r, x in enumerate(stack):
            nxt_board[r][c] = x[0]
else: # 'D'
    for c in range(N):
        stack = []
        for r in range(N - 1, -1, -1):
            num = board[r][c]
            if num == 0: continue

            if stack and stack[-1][0] == num and stack[-1][1] == False:
                stack[-1] = [num * 2, True]
            else:
                stack.append([num, False])

        for r, x in enumerate(stack):
            nxt_board[N-r-1][c] = x[0]

print('\n'.join( [' '.join(map(str, line)) for line in nxt_board ] ))

