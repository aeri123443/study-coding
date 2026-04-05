'''
민트 초코 우유: 2025 상반기 오전 1번 문제
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/mint-choco-milk/description

문제 읽기: 10m
문제 분석: 12m
코드 작성: 2h 13m
오류 확인 및 수정: 0m

총 소요 시간: 2h 35m
'''

from pprint import pprint
import heapq

# 전역 변수 관리
N, T = 0, 0
INF = float('inf')
p_heapq = [] # 대표자 힙큐
f_board = [] # 신봉 음식 관리
b_board = [] # 신앙심 관리
visited = [] # 방문 배열 (전파 여부 관리)
move = [ (-1, 0), (1, 0), (0, -1), (0, 1) ]

# 신봉 음식 매핑
f_mapping = {
    'T': (1, 0, 0),
    'C': (0, 1, 0),
    'M': (0, 0, 1),
}

# 항목에 따른 점수 계산
scores = {
    (1, 1, 1): 0,
    (1, 1, 0): 0,
    (1, 0, 1): 0,
    (0, 1, 1): 0,
    (0, 0, 1): 0,
    (0, 1, 0): 0,
    (1, 0, 0): 0,
}
# 항목에 따른 매핑 인덱스
f_idx = {
    (1, 1, 1): 0,
    (1, 1, 0): 1,
    (1, 0, 1): 2,
    (0, 1, 1): 3,
    (0, 0, 1): 4,
    (0, 1, 0): 5,
    (1, 0, 0): 6,
}

## 값 입력
def data_input():
    global N, T, f_board, b_board, visited

    N, T = map(int, input().split())
    # 신봉 음식 입력
    # f_board = [ list(input().strip()) for _ in range(N) ]
    for i in range(N):
        tmp_list = []
        for x in list(input().strip()):
            tmp_list.append( f_mapping[x] )
        f_board.append(tmp_list)

    # 신앙심 입력
    b_board = [ list(map(int, input().split())) for _ in range(N) ]
    # 방문 배열 생성
    visited = [ [False]*N for _ in range(N) ]

## visited 데이터 초기화
def visited_init():
    for i in range(N):
        for j in range(N):
            visited[i][j] = False

## score 데이터 초기화
def scores_init():
    for k in scores.keys():
        scores[k] = 0
## 아침
def morning():
    # 모든 학생의 신앙심이 1 증가
    for i in range(N):
        for j in range(N):
            b_board[i][j] += 1

# 같은 그룹의 좌표를 반환
def grouping(si, sj, f, r):
    result = r

    # 다음 좌표가 이동 가능하고 같은 음식이면
    for di, dj in move:
        ni, nj = si + di, sj + dj
        if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and f_board[ni][nj]==f:
            # 그룹에 좌표 추가
            result.append((ni, nj))
            # 다음으로 진행
            visited[ni][nj] = True
            grouping(ni, nj, f, result)
    # 그룹 반환
    return result

# 그룹 내 대표자를 찾고 신앙심 업데이트
def find_president(pos_list):
    n = len(pos_list)
    p = (INF, INF, INF) # -b, r, c

    # 대표자 업데이트
    for r, c in pos_list:
        p = min(p, (-b_board[r][c], r, c))
    # print(p)

    # 신앙심 업데이트
    for r, c in pos_list:
        if (r, c) == (p[1], p[2]):
            b_board[r][c] += (n-1)
        else:
            b_board[r][c] -= 1

    # 업데이트된 p 정보를 반환
    pr, pc = p[1], p[2]
    return (-b_board[pr][pc], pr, pc)

## 점심
def afternoon():
    for i in range(N):
        for j in range(N):
            # 아직 확인하지 않았다면 진행
            if not visited[i][j]:
                # 대표자 기준 = (-신앙심, r, c)
                # b = (-b_board[i][j], i, j)
                visited[i][j] = True
                # 같은 그룹의 좌표를 반환
                pos_list = grouping(i, j, f_board[i][j], [(i,j)])
                # 대표자 선정 및 신앙심 업데이트
                p = find_president(pos_list)

                # heapq에 담기
                pb, pr, pc = p
                # q_data = (그룹, -신앙심, r, c)
                q_data = (sum(f_board[i][j]), pb, pr, pc)
                heapq.heappush(p_heapq, q_data )

## 전파
def explore(x, f, si, sj, di, dj):
    ni, nj = si + di, sj + dj

    # 이동 가능한 좌표이고, x가 0 초과이며, 신봉 음식이 다른지?
    # print('dd  ', ni, nj, x, f_board[ni][nj], f)
    if 0<=ni<N and 0<=nj<N and x>0:
        if f_board[ni][nj]!=f:
            y = b_board[ni][nj]
            # 전파 당함 체크
            visited[ni][nj] = True

            # 강한 전파
            if x > y:
                # print('  강한 전파 ', ni, nj)
                f_board[ni][nj] = f

                x -= (y+1)
                b_board[ni][nj] += 1
            # 약한 전파
            else:
                # print('  약한 전파 ', ni, nj)

                # or 연산
                tx, cx, mx = f
                ty, cy, my = f_board[ni][nj]
                nf = ( (tx|ty), (cx|cy), (mx|my) )
                f_board[ni][nj] = nf

                b_board[ni][nj] += x
                x = 0

        explore(x, f, ni, nj, di, dj)


def evening():
    # 대표자 순서대로 진행
    while p_heapq:
        g, b, r, c = heapq.heappop(p_heapq)
        # print('이번 대표자: ' , g, b, r, c)
        b = -b

        # 전파 당했으면 그날 전파를 진행할 수 없음
        if visited[r][c]:
            continue

        # 대표자 신앙심 업데이트
        x = b-1
        b_board[r][c] = 1

        # 방향 결정 및 전파 시작
        di, dj = move[ b%4 ]
        # print(':: di, dj ::')
        # print(di, dj)
        f = f_board[r][c]
        explore(x, f, r, c, di, dj)
        # print(':: f_board ::')
        # pprint(f_board)
        # print(':: b_board ::')
        # pprint(b_board)
        # print(':: visited ::')
        # pprint(visited)

## 점수 계산
def cal_score():
    for i in range(N):
        for j in range(N):
            # 해당 좌표의 f, b를 뽑아내고
            f, b = f_board[i][j], b_board[i][j]
            # score에 업데이트
            scores[f] += b
    # print(scores)

## 점수 반환
def print_scores():
    answer = [-1]*7

    for k, v in scores.items():
        idx = f_idx[k]
        answer[idx] = v

    print( ' '.join(map(str, answer)) )
#### 메인 로직 ####

## 값 입력
data_input()
# pprint(f_board)
# pprint(b_board)
# pprint(visited)

for t in range(T):
    # print("####################################################################")
    # print("T = ", t+1)
    # print("####################################################################")

    ## 데이터 초기화
    visited_init()
    scores_init()
    # print('visited_init...')
    # pprint(f_board)
    # pprint(b_board)
    # pprint(visited)
    # pprint(scores)
    # print("------------------------------------")

    ## 아침 신앙심 증가
    morning()
    # print('morning...')
    # pprint(f_board)
    # pprint(b_board)
    # pprint(visited)
    # print("------------------------------------")

    ## 점심 - 대표자 선정
    afternoon()
    visited_init()
    # print('afternoon...')
    # print(':: p_heapq ::')
    # pprint(p_heapq)
    # print(':: f_board ::')
    # pprint(f_board)
    # print(':: b_board ::')
    # pprint(b_board)
    # print(':: visited ::')
    # pprint(visited)
    # print("------------------------------------")

    ## 저녁 - 전파 시작
    # print('evening...')
    evening()
    # print(':: p_heapq ::')
    # pprint(p_heapq)
    # print(':: f_board ::')
    # pprint(f_board)
    # print(':: b_board ::')
    # pprint(b_board)
    # print(':: visited ::')
    # pprint(visited)

    ## 점수 계산 및 반환
    cal_score()
    print_scores()