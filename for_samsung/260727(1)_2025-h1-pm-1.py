'''
미생물 연구: 2025 상반기 오후 1번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/microbial-research/description

문제 분석: 11m 06s
코드 1차 작성: 2h 22m 0s
  - [tc3 fail] 분할 영역에서 영역이 0이 되었을 때에는 삭제 처리를 안 해주고 있었는데, 이 부분이 누적되면서 오류가 발생
디버깅 및 코드 2차 작성: 13m 01s

총 소요 시간: 2h 46m 07s
'''

from collections import deque, defaultdict

class Item:
    def __init__(self, num, x1, y1, x2, y2):
        self.num = num
        self.sr = y1
        self.sc = x1
        self.relative = [(r-y1, c-x1) for r in range(y1, y2) for c in range(x1, x2)]

N, Q = -1, -1
MOVE = [(0, +1), (0, -1), (+1, 0), (-1, 0)]
INF = float('inf')

###############################################################
#### 보조 함수
###############################################################

### 미생물 투입, 겹칠 경우 덮어쓰기
def input_item(num, items, input_board, x1, y1, x2, y2):
    item = Item(num, x1, y1, x2, y2)
    items[num] = item

    for r in range(y1, y2):
        for c in range(x1, x2):
            input_board[r][c] = num

### 전체 영역 탐색 (bfs)
def explore_area(visited, input_board):
    def bfs(num, sr, sc):
        q = deque([(sr, sc)])
        visited[sr][sc] = True

        while q:
            cr, cc = q.popleft()

            for dr, dc in MOVE:
                nr, nc = dr+cr, dc+cc

                if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and input_board[nr][nc]==num and input_board[nr][nc]!=-1:
                    visited[nr][nc] = True
                    q.append((nr,nc))

    # visited 초기화
    for i in range(N):
        for j in range(N):
            visited[i][j] = False

    # 영역 기록 좌표
    areas_info = defaultdict(int)

    # 방문하지 않은, 새로운 번호가 나오면 bfs 시작
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and input_board[i][j] != -1 :
                num = input_board[i][j]
                areas_info[num] += 1
                bfs(num, i, j)

    return areas_info

### 이동 가능한 영역 탐색 및 시작 좌표 반환
def find_move_item(move_board, item):
    relatives = item.relative

    for c in range(N):
        for r in range(N):
            # 각 좌표를 시작 기점으로, 미생물을 배치할 수 있는지 확인
            flag = False
            for dr, dc in relatives:
                nr, nc = dr+r, dc+c
                if 0<=nr<N and 0<=nc<N and move_board[nr][nc]==-1:
                    continue
                else:
                    flag = True
                    break
            if not flag:
                return r, c

    return -1, -1

# 미생물 이동 및 상태 업데이트
def move_item(move_board, item, sr, sc):

    for dr, dc in item.relative:
        nr, nc = dr + sr, dc + sc
        move_board[nr][nc] = item.num

    item.r = sr
    item.c = sc

### 미생물 상태 업데이트
def update_item_position(items, num, input_board, visited, sr, sc):
    item = items[num]
    min_r, min_c = sr, sc
    absolute = [(sr, sc)] # 절대 좌표 저장

    for i in range(N):
        for j in range(N):
            visited[i][j] = False

    q = deque([(sr, sc)])
    visited[sr][sc] = True

    while q:
        cr, cc = q.popleft()

        for dr, dc in MOVE:
            nr, nc = dr+cr, dc+cc

            if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
                visited[nr][nc] = True
                # 같은 번호면 좌표 업데이트
                if input_board[nr][nc] == num:
                    absolute.append((nr, nc))
                    min_r = min(min_r, nr)
                    min_c = min(min_c, nc)
                    q.append((nr, nc))

    # 상대좌표 업데이트
    relative = [ (ar-min_r, ac-min_c) for ar, ac in absolute]

    # 미생물 상태 업데이트
    item.r = min_r
    item.c = min_c
    item.relative = relative

### 인접한 영역 탐색 및 반환
def find_neighbor(move_board):
    neighbor_set = set()

    # 이전 칸과 다음 칸이 다를 때를 체크
    for r in range(N):
        for c in range(N):
            cur_num = move_board[r][c]
            if cur_num == -1: continue

            for dr, dc in [(0,+1), (+1,0)]:
                nr, nc = dr+r, dc+c
                if 0<=nr<N and 0<=nc<N and move_board[nr][nc]!= -1 and move_board[nr][nc]!=cur_num:
                    neighbor_set.add( ( min(move_board[nr][nc], cur_num), max(move_board[nr][nc], cur_num)   ) )

    return neighbor_set
###############################################################
#### 메인 로직
###############################################################
def main():
    global N, Q

    N, Q = map(int, input().split())
    items = {}
    input_board = [[-1]*N for _ in range(N)]
    move_board = [[-1]*N for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    answer = []

    for q in range(Q): # q: 미생물 번호
        x1, y1, x2, y2 = map(int, input().split())

        ### 1단계: 미생물 투입 ###
        # 미생물 투입, 겹칠 경우 덮어쓰기
        input_item(q, items, input_board, x1, y1, x2, y2)
        # 전체 영역 탐색
        areas_info = explore_area(visited, input_board)

        # print()

        # 영역이 두 개일 경우 사라짐 처리 -> 후처리
        remove_set = set()
        for i, v in areas_info.items():
            if v > 1:
                remove_set.add(i)
                del items[i]
        for i in range(N):
            for j in range(N):
                if input_board[i][j] in remove_set:
                    input_board[i][j] = -1


        # 남은 미생물에 대해, 전체 위치 정보 업데이트
        updated_set = set()
        for i in range(N):
            for j in range(N):
                num = input_board[i][j]
                if num!=-1 and not num in updated_set:
                    updated_set.add(num)
                    update_item_position(items, num, input_board, visited, i, j)

        # 아예 사라져 영역이 잡히지 않은 부분도 확인
        del_keys = []
        for k in items.keys():
            if k not in updated_set:
                del_keys.append(k)
        for k in del_keys: del items[k]

        # print()

        ### 2단계: 배양 용기 이동 ###
        # 이동 순서 정하기
        sorted_items = sorted([ (-len(item.relative), item.num) for item in items.values() ])
        for _, num in sorted_items:
            item = items[num]

            # 이동 가능한 영역 탐색 및 시작 좌표 반환
            tsr, tsc = find_move_item(move_board, item)
            # 이동 불가할 경우 미생물 삭제
            if tsr == -1:
                del items[num]
            else:
                # 미생물 이동 및 시작좌표 업데이트
                move_item(move_board, item, tsr, tsc)
            # print()

        ### 3단계: 결과 기록 및 초기화
        # 인접한 영역 탐색 및 반환
        neighbor_set = find_neighbor(move_board)
        total = 0
        for a, b in neighbor_set:
            total += ( len(items[a].relative) * len(items[b].relative) )
        answer.append(str(total))
        # print()

        for i in range(N):
            for j in range(N):
                input_board[i][j] = move_board[i][j]
                move_board[i][j] = -1
        # print()
    print('\n'.join(answer))

main()