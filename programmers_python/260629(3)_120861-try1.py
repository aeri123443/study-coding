'''
120861. 캐릭터의 좌표
https://school.programmers.co.kr/learn/courses/30/lessons/120861

문제 분석: 6m 48s
코드 작성: 9m 5s
디버깅: 4m 14s
total: 20m 8s
'''

MOVE = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, +1)
}
def solution(keyinput, board):
    w, h = board
    min_i, max_i = -(h//2), +(h//2)
    min_j, max_j = -(w//2), +(w//2)
    ci, cj = 0, 0

    for cmd in keyinput:
        di, dj = MOVE[cmd]
        ni = di + ci
        nj = dj + cj
        if min_i <= ni <= max_i and min_j <= nj <= max_j:
            ci, cj = ni, nj

    return [cj, -ci]

print(solution(["left", "right", "up", "right", "right"],	[11, 11]))
print(solution(["down", "down", "down", "down", "down"],	[7, 9]))
