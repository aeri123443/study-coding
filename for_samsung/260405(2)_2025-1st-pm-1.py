'''
미생물 연구: 2025 상반기 오후 1번 문제
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/microbial-research/description

나중에 다시 풀어보자,, ㅠㅠ
'''

from pprint import pprint
import heapq
from collections import deque

## 전역변수 관리
N, Q = 0, 0
areas = {} # 영역 번호: [넓이, 상대위치 {(y,x), (y,x), ...}, 기준 좌표(sy, sx)]
first_board = [] # 투입하는 용기
second_board = [] # 옮기는 용기
move = [ (1,0), (-1,0), (0,1), (0,-1)]

## 값 입력 및 초기 데이터 구성
def input_data():
    global N, Q, areas, first_board, second_board

    N, Q = map(int, input().split())
    first_board = [[-1]*N for _ in range(N)]
    second_board = [[-1]*N for _ in range(N)]

## 데이터 초기화
def init_data():
    global first_board

    for x in range(N):
        for y in range(N):
            first_board[y][x] = second_board[y][x]
            second_board[y][x] = -1

## 상대위치와 시작위치를 활용하여 미생물 배치
def put_items(board, sx, sy, q):
    for dy, dx in areas[q][1]:
        nx, ny = sx + dx, sy + dy
        board[ny][nx] = q

## 미생물 그룹이 분리되었는지 확인
def is_separated(board, q, sx, sy):
    cnt = 0
    dq = deque( [(sy, sx)] )

    # 상대좌표에 대한 실제 좌표 담기
    item_pos = set()
    for dy, dx in areas[q][1]:
        nx, ny = sx + dx, sy + dy
        item_pos.add((ny, nx))

    # 상하좌우로 이동
    while dq:
        (cy, cx) = dq.popleft()
        if (cy, cx) in item_pos:
            item_pos.remove((cy, cx))

        for dy, dx in move:
            nx, ny = cx + dx, cy + dy

            if (ny, nx) in item_pos:
                item_pos.remove((ny, nx))
                dq.append((ny, nx))

    # 분리되었으면(item_pos에 값이 남아있으면) True 반환
    return True if item_pos else False

## 미생물 제거
def remove_items(board, q):
    for x in range(N):
        for y in range(N):
            if board[y][x] == q:
                board[y][x] = -1

    del areas[q]

## 투입
def input_items(q):
    areas[q] = [0, {}, ()]

    r1, c1, r2, c2 = map(int, input().split())
    r = r2 - r1
    c = c2 - c1

    # area 넓이, 기준좌표 업데이트
    areas[q][0] = r * c
    areas[q][2] = (c, r)

    # area 상대 위치 업데이트
    tmp_set = set()
    for x in range(r):
        for y in range(c):
            tmp_set.add( (y,x) )
    areas[q][1] = tmp_set

    # 덮어쓰면서, 덮어써진 다른 미생물이 있는지 확인
    check_set = set()
    sx, sy = r1, c1
    for dy, dx in areas[q][1]:
        nx, ny = sx + dx, sy + dy

        other = first_board[ny][nx]
        if other >= 0:

            # 삭제되는 상대좌표
            ssy, ssx = areas[other][2]
            rx, ry = nx - ssx, ny - ssy

            # area 업데이트
            areas[other][0] -= 1
            areas[other][1].remove( (ry, rx) )

            check_set.add( other )

        first_board[ny][nx] = q

    # 덮어써진 애들 나뉘었나 확인 후 제거
    for other in check_set:
        if areas[other][0] == 0:
            del areas[other]
            continue
        tmp_cy, tmp_cx = areas[other][2]
        tmp_ry, tmp_rx = next(iter(areas[other][1]))

        if is_separated(first_board, other, tmp_cx+tmp_rx, tmp_cy+tmp_ry):
            remove_items(first_board, other)

## 미생물을 놓을 수 있는지 확인
def explore_empty(sx, sy, q):
    for dy, dx in areas[q][1]:
        nx, ny = sx + dx, sy + dy

        # 이동 가능 좌표, 빈 공간인지 확인
        if 0<=nx<N and 0<=ny<N and second_board[ny][nx] == -1:
            continue
        else:
            return False

    return True

## 미생물 이동
def move_items():
    # 미생물 이동 순서 정하기
    hq = []
    for k, v in areas.items():
        heapq.heappush(hq, (-v[0], k)) # (넓이, 먼저 투입)

    while hq:
        _, q = heapq.heappop(hq)

        # 비어있는 (y,x)에 대하여 넣을 수 있는지 탐색
        flag = False
        for x in range(N):
            if flag:
                break
            for y in range(N):
                if second_board[y][x] == -1:
                    if explore_empty(x, y, q):
                        # 넣을 수 있을 경우 넣기
                        put_items(second_board, x, y, q)
                        # 기준 좌표 업데이트
                        areas[q][2] = (y, x)
                        flag = True
                        break

        # 한 번도 걸리지 않음 = 넣을 수 없는 경우
        # 미생물 제거
        if not flag:
            del areas[q]

## 인접한 영역 탐색 및 반환
def bfs(board, visited, sx, sy):
    q = board[sy][sx]
    neighbor = set()

    dq = deque()
    dq.append((sy, sx))
    visited[sy][sx] = True

    while dq:
        cy, cx = dq.popleft()

        for dy, dx in move:
            nx, ny = cx + dx, cy + dy
            if 0<=nx<N and 0<=ny<N and not visited[ny][nx] and board[ny][nx] >= 0:
                # q랑 같으면 계속 진행
                if board[ny][nx] == q:
                    visited[ny][nx] = True
                    dq.append((ny, nx))
                # q랑 다르면 neighbor에 추가 후 멈춤
                else:
                    if board[ny][nx] not in neighbor:
                        neighbor.add(board[ny][nx])

    return neighbor

## 성과 계산
def cal_score():
    visited = [[False]*N for _ in range(N)]
    answer = 0

    for x in range(N):
        for y in range(N):
            if second_board[y][x] >= 0 and not visited[y][x]:
                neighbor = bfs(second_board, visited, x, y)
                # print(x, y, second_board[y][x], 'neighbor...', neighbor)
                if len(neighbor) > 0:
                    k1 = second_board[y][x]
                    v1 = areas[k1][0]

                    for k2 in neighbor:
                        v2 = areas[k2][0]
                        answer += (v1*v2)

    print(answer)

########## 메인 로직 ##########

## 값 입력
input_data()
# print('input_data...')

for q in range(Q):
    # print('q...', q)
    ## 데이터 초기화
    init_data()
    print('init_data...')

    ## 투입
    input_items(q)
    print('input_items...')

    # 이동
    move_items()
    print('move_items...')

    # 계산
    cal_score()
    print('cal_score...')
