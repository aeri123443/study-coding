"""
🔗 [픽셀 아트](https://edu.codetree.ai/samsung-camp/class/439/learn/lecture/4804/curated-cards/mock-grid-coloring/description)
## ⏱ 풀이 시간
- 총 소요 시간: 2h 17m 39s
	- 문제 분석: 43m 00s
	- 코드 작성: 1h 34m 39s
	- 시간 초과
"""

# N * N (2~200) 1-index
# RGB 0~255
#
# Q(1~200)번 반복 -> 최종 캔버스 모습 출력
#
# 1. 물방울 도구
#   - 100 x y w(<=2N)
#   - 물방울: 좌표 x,y 퍼짐 정도 w
#   - 색상 변화 맨해튼 거리 d = 0~w
#       |-| + |-|
#     - 다음 거리에 픽셀 하나 이상 존재
#       - 존재 x -> 확산 중단
#       - if 존재
#         - 색상값//2 남김(100,100,100 -> 50,50,50), 나머지 색상값은 확산량
#         - (거리가 d인 모든 픽셀에서 퍼져나갈 색상RGB 각각의 합) // (거리 d+1) 픽셀 개수
#           [?] 거리가 d인 ~ 이 결국 50아닌가? 뭘 굳이 합하지?
#         - d+1 각 픽셀의 RGB에 더함, *** max 255
#         - w 거리도 전달되면 종료
# 2. 마법 지우개
#   - 200 c(RGBW)
#   - 특정 색상 영역 중 가장 넓은 부분을 검은색(000)으로
#     1) 빨 영역: R > G+B 인 픽셀
#     2) 초 영역: G > R+B 인 픽셀
#     3) 파 영역: B > R+G 인 픽셀
#     4) 흰 영역: R, G, B >= 128 인 픽셀
#     5) 기타 영역: else
#   - RGBW 영역 찾기
#   - 가장 큰 영역 -> 검은색으로
#     ** 둘 이상 영역 -> 모두 검정
#   - 검은색이 된 픽셀 총 개수를.. 한줄에?? 한개가 아냐?
#
# 확인 케이스
# - 우선순위 잘 지키는지 (기타영역 잘 걸러지는지)
# - 물방울에서 확산 시 255 최댓값 잘 지켜지는지
# - 색상값이 변경되는 모든 영역에서 색상 재판정
# - 확산 거리 2일 때
#
# 설계
# for Q
#     # 1. 물방울 도구
#     - 100 x y w(<=2N)
#     - 물방울: 좌표 x,y 퍼짐 정도 w
#     - 색상 변화 맨해튼 거리 d = 0~w
#     for d(0~w)
#         nr, nc 멘해튼 거리
#         move_next_pos[] # 이동 가능한 다음 거리 반환
#         - 다음 거리에 픽셀 하나 이상 존재
#         - 존재 x -> 확산 중단
#         - if 존재
#             - 색상값//2 남김(100,100,100 -> 50,50,50), 나머지 색상값은 확산량
#             - (거리가 d인 모든 픽셀에서 퍼져나갈 색상RGB 각각의 합) // (거리 d+1) 픽셀 개수
#             [?] 거리가 d인 ~ 이 결국 50아닌가? 뭘 굳이 합하지?
#             - d+1 각 픽셀의 RGB에 더함, *** max 255
#             # RGB 정보 업데이트
#             - w 거리도 전달되면 종료
#             [?] 다음 거리로 나가도 확산량은 유지되는지?
#     2. 마법 지우개
#     - 200 c(RGBW)
#     - 특정 색상 영역 중 가장 넓은 부분을 검은색(000)으로
#         1) 빨 영역: R > G+B 인 픽셀
#         2) 초 영역: G > R+B 인 픽셀
#         3) 파 영역: B > R+G 인 픽셀
#         4) 흰 영역: R, G, B >= 128 인 픽셀
#         5) 기타 영역: else
#     # 색상 영역 확인
#         max_num, max_path
#         for r, c
#             board[r][c] == 색상 -> find_area
#             max_num 같으면 path append
#             크면 update
#     - RGBW 영역 찾기
#     - 가장 큰 영역 -> 검은색으로
#         ** 둘 이상 영역 -> 모두 검정
#     - 검은색이 된 픽셀 총 개수를.. [?] 한줄에?? 한개가 아냐? -> \n 포함하란 뜻
# 이해 및 설계 43:00

# 시간초과, but 시간관계상 일단 다음 문제로 넘어감
from collections import deque

DEBUG = False
N = int(input())
MOVE = [(0,1), (1,0), (0,-1), (-1,0)]
value_board = [[[0,0,0] for _ in range(N)] for _ in range(N)]
color_board = [['B']*N for _ in range(N)]
for co in range(3):
    for r in range(N):
        tmp = list(map(int, input().split()))
        for c in range(N):
            value_board[r][c][co] = tmp[c]
# 여기까지 입력 코드 작성 7:48

# 각 칸의 RGB 판정
def update_color(r, c): # 9:24
    v_r, v_g, v_b = value_board[r][c]

    if v_r > v_g + v_b: color = "R"
    elif v_g > v_r + v_b: color = "G"
    elif v_b > v_r + v_g: color = "B"
    elif v_b >= 128 and v_r >= 128 and v_g >= 128: color = "W"
    else: color = 'E' # else

    color_board[r][c] = color

for r in range(N):
    for c in range(N):
        update_color(r,c)
# if DEBUG: print()

# 다음 좌표 중 맨해튼 거리 & 이동 가능 좌표 반환
def get_next_pos(cur_pos, sr, sc, dis):
    path = set()
    for cr, cc in cur_pos:
        for dr, dc in MOVE:
            nr, nc = cr+dr, cc+dc
            if 0<=nr<N and 0<=nc<N and dis == (abs(nr-sr) + abs(nc-sc)):
                path.add((nr, nc))
    return path

# 1. 물방울 도구
def drop_water(line): # 27:50
    x, y, w = map(int, line)
    sr, sc = x-1, y-1

    cur_pos = {(sr, sc)}
    for dis in range(1, w+1):
        next_pos = get_next_pos(cur_pos, sr, sc, dis)
        if not next_pos: break

        # 각각의 확산값 합 구하기
        # 색상값//2 남김(100,100,100 -> 50,50,50), 나머지 색상값은 확산량
        # [?] 거리가 d인 모든 픽셀에서 퍼져나갈 색상RGB 각각의 합?? 뭘 굳이 합하지?
            # 이 부분 늦게 이해해서 코드 추가 수정 + tc 만들고 디버깅까지 28:08
        d_color = [0,0,0]
        for cr, cc in cur_pos:
            for co in range(3):
                remain = value_board[cr][cc][co] // 2
                d_color[co] += value_board[cr][cc][co] - remain
                value_board[cr][cc][co] = remain

        # 실제 확산량 구하기
        for co in range(3):
            d_color[co] //= len(next_pos)

        # 확산
        for nr, nc in next_pos:
            for co in range(3):
                value_board[nr][nc][co] = min(255, value_board[nr][nc][co]+d_color[co])

        cur_pos = next_pos
# bfs: 해당 위치 기준, 색상 영역 반환
def find_area(sr,sc,target_color, visited):
    q = deque([(sr, sc)])
    visited[sr][sc] = True
    pos = {(sr,sc)}

    while q:
        cr, cc = q.popleft()

        for dr, dc in MOVE:
            nr, nc = dr+cr, dc+cc
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and color_board[nr][nc] == target_color:
                pos.add((nr,nc))
                visited[nr][nc] = True
                q.append((nr,nc))

    return pos

# 2. 마법 지우개
def magic_eraser(line): # 14:20
    target_color = line[0]
    max_num = -1
    max_pos = set()

    for r in range(N):
        for c in range(N):
            update_color(r, c)

    visited = [[False] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if color_board[r][c] == target_color:
                pos = find_area(r,c,target_color, visited)
                # max_num 같으면 max_pos add
                if max_num == len(pos):
                    max_pos.update(pos)
                elif max_num < len(pos):
                    max_num = len(pos)
                    max_pos = pos

    # 가장 큰 영역(둘 이상 ok) -> 검은색으로
    for r, c in max_pos:
        value_board[r][c] = [0,0,0]
        color_board[r][c] = 'E'

    return len(max_pos)

Q = int(input())
answer = []
for _ in range(Q):
    cmd, *line = input().split()

    if cmd == '100':
        drop_water(line)

    elif cmd == '200':
        max_pos = magic_eraser(line)
        answer.append(max_pos)

    if DEBUG: print()
print('\n'.join(map(str, answer)))

# 전체 보드 출력
for r in range(N):
    row = []
    for c in range(N):
        row.append(sum(value_board[r][c]))
    print(' '.join(map(str, row)))
