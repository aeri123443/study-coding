'''
아기 고래의 첫 항해:  2026 상반기 오후 1번 문제
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/baby-whale-first-voyage/description
문제 분석: 22m 12s
코드 작성: 2h 03m 38s
디버깅: 3m 05s -> 2단계에서 목표 좌표 찾을 때 inf 좌표 오류 발생: 1단계에서 탐색이 완료되었을 때, 2단계로 넘어가지 않도록 설정

총 소요 시간: 2h 28m 56s
'''

from collections import deque

############################################################
##### 전역 변수 선언
############################################################

N = -1 # 행과 열 길이
target_len = -1 # 방문 가능한 바다 칸 수 (전체 칸 수 - 암초 수)
board = [] # 방문X 0, 암초 1, 방문O 2
MOVE = [None, (-1,0), (+1, 0), (0,-1), (0,+1)]
INF = float('inf')
############################################################
##### 보조 함수
############################################################

### 0단계: 데이터 입력
def input_data():
    global N, target_len, board

    N, r, c, d = map(int, input().split())

    target_len = N*N
    for i in range(N):
        tmp = list(map(int, input().split()))
        target_len -= tmp.count(1)
        board.append(tmp)

    return r, c, d

### 1단계: 인접 탐험
def explore_neighbor(answer, sr, sc, sd):
    # 다음 방향 매핑
    d_guide = [
        None,
        [1,3,4,2],
        [2,4,3,1],
        [3,2,1,4],
        [4,1,2,3],
    ]

    cr, cc, cd = sr, sc, sd
    if board[cr][cc] == 0:
        answer.append( (cr, cc) )
        board[cr][cc] = 2

    while True:
        # 인접한 곳에 이동 가능한 곳이 없으면 탈출
        flag = True

        # 우선순위(방향) 기준 인접한 곳으로 이동 (바라보는 방향 고려)
        for d_idx in d_guide[cd]:
            dr, dc = MOVE[d_idx]
            nr, nc = cr+dr, cc+dc

            # 범위, 장애물, 방문여부
            if 0<=nr<N and 0<=nc<N and board[nr][nc]==0:
                answer.append( (nr,nc) )
                board[nr][nc] = 2
                cr, cc, cd = nr, nc, d_idx
                flag = False
                break

        if flag: break

    return cr, cc, cd

###  2단계: 가까운 바다로 이동

## 2-1 목표 좌표 찾기
def find_next(sr, sc):

    q = deque([ (sr, sc, 0)] )
    tmp_visited = { (sr, sc) }
    min_visited = [INF, (INF, INF)] # (cnt, r, c)

    while q:
        cr, cc, cnt = q.popleft()
        # print('cr, cc:', cr, cc)

        if cnt >= min_visited[0]:
            continue

        for dr, dc in MOVE[1:]:
            nr, nc = dr+cr, dc+cc
            # print('  nr, nc:', nr, nc)

            # 범위 내, tmp_visited, 장애물
            if 0<=nr<N and 0<=nc<N and (nr, nc) not in tmp_visited and board[nr][nc]!=1:
                # 아직 방문하지 않았으면 해당 좌표를 목표 지점 후보로 지정
                if board[nr][nc] == 0 and cnt+1 <= min_visited[0] and (nr,nc) < min_visited[1]:
                    min_visited = [cnt+1, (nr,nc)]
                    # print('    min_visited: ', min_visited)

                q.append( (nr, nc, cnt+1) )
                # print('    append: ', nr, nc, cnt+1)

                tmp_visited.add( (nr, nc) )

    return min_visited[1]
    # 우선순위 기준 목적지 좌표 선정
    # 우선순위 기준 이동

## 2-2 목표 좌표로 이동하는 경로 찾기
def find_target_route(sr, sc, tr, tc):

    visited_parent = { (sr, sc): (-1, -1) }
    q = deque([(sr, sc)])

    while q:
        cr, cc = q.popleft()

        for d_idx in [3,2,4,1]:
            dr, dc = MOVE[d_idx]
            nr, nc = dr+cr, dc+cc

            # 범위, 장애물, visited_parent
            if 0<=nr<N and 0<=nc<N and board[nr][nc]!=1 and (nr, nc) not in visited_parent:
                visited_parent[ (nr,nc) ] = (cr, cc)

                if nr==tr and nc==tc: break

                q.append((nr,nc))

    # 방문 경로 반환
    # print(visited_parent)
    target_route = [(tr, tc)]
    cr, cc = tr, tc
    while cr!=sr or cc!=sc:
        # print('cr, cc ', cr, cc)
        cr, cc = visited_parent[(cr, cc)]
        # print('nr, nc ', cr, cc)

        target_route.append( (cr, cc) )

    return target_route[::-1]

## 2-3 목표 경로대로 이동
def move_target(answer, target_route):

    # 방문 체크 및 정답 누적
    for r, c in target_route:
        if board[r][c] == 0:
            board[r][c] = 2
            answer.append( (r,c) )

    # 마지막 방향 반환
    d_guide = {(-1,0):1, (+1,0):2, (0,-1):3, (0,+1):4}
    r_end, c_end = target_route[-1]
    r_prv, c_prv = target_route[-2]

    return d_guide[( r_end-r_prv, c_end-c_prv )]

### 3단계: 정답 출력은 1씩 더해서
def print_answer(answer):
    tmp = [' '.join(map(str, [a+1, b+1])) for a, b in answer]
    print( '\n'.join(tmp)   )

############################################################
##### 메인 로직
############################################################

def main():
    answer = []  # 방문 순서를 set으로 관리

    # 0단계: 데이터 입력, r과 c는 편의상 1 빼고 수행
    sr, sc, sd = input_data()
    cr, cc, cd = sr-1, sc-1, sd
    # print()

    # 모든 바다 방문 시 탐색 종료
    while len(answer) < target_len:
        # 1단계: 인접 탐험
        cr, cc, cd = explore_neighbor(answer, cr, cc, cd)
        # print()
        if len(answer) >= target_len: break

        # 2단계: 가까운 바다로 이동
        ## 2-1 목표 좌표 찾기
        tr, tc = find_next(cr, cc)
        # print()

        ## 2-2 목표 좌표 경로 찾기
        target_route = find_target_route(cr, cc, tr, tc)
        # print()

        ## 2-3 목표 경로대로 이동
        cd = move_target(answer, target_route)
        cr, cc = tr, tc
        # print()

    # 3단계: 정답 출력은 1씩 더해서
    print_answer(answer)

if __name__ == '__main__':
    main()