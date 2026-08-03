'''
개구리의 여행: 2025 상반기 오전 2번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/frog-journey

문제 분석: 26m 19s
코드 1차 작성: 1h 06m 08s
  - [시간 소요] 조건 누락 - 점프력 증가는 1씩만 가능하다는 차이를 누락하여, 문제를 다시 이해하는 데 시간이 낭비됨.
코드 디버깅: 22m 35s
  - [TC34 fail] 시간 초과 - 다익스트라의 조기 탈출 조건을 명시하지 않음.

총 소요 시간: 1h 55m 02s
'''

import heapq

####################################################################
##### 전역 선언
####################################################################

INF = float('inf')
MAX_K = 5
MOVE = [(+1,0), (-1,0), (0,+1), (0,-1)]
N, Q = -1, -1

q = []
board = []
visited = []

####################################################################
##### 보조 함수
####################################################################

# 1idx -> 0idx
def make_0_idx(x):
    return x-1

# 범위 확인
def is_range(r, c):
    return 0<=r<N and 0<=c<N

# 기본 데이터 입력
def input_data():
    global N, Q, board, visited
    N = int(input())
    board = [list(input()) for _ in range(N)]
    Q = int(input())
    visited = [[[INF]*6 for _ in range(N)] for _ in range(N)] # 점프력 1~k으로 왔을 때, 0은 패딩

# 디버깅 출력
def debug_q():
    print()
    debug_print = []
    for i in range(N):
        tmp_line = []
        for j in range(N):
            tmp = board[i][j] + ' ' + str(visited[i][j])
            tmp_line.append(tmp)
        debug_print.append('\t\t'.join(tmp_line))
    print('\n'.join(debug_print))

# 해당 방향으로 이동하면서, 착지 가능한 좌표에 해당하는 점프량을 반환
def find_jump_k(cr, cc, dr, dc):
    k_list = []

    for k in range(1,6):
        nr, nc = cr + dr*k, cc + dc*k
        if is_range(nr, nc):
            # 안전한 돌이면 착지 가능
            if board[nr][nc] == '.':
                k_list.append(k)
            # 미끄러운 돌이면 지나갈 수는 있음
            # 천적이 있으면 탐색 종료
            elif board[nr][nc] == '#':
                break
        else: break

    return k_list

####################################################################
##### 메인 로직
####################################################################
def main():
    global q
    input_data()

    answer = []

    for _ in range(Q):
        sr, sc, er, ec = map(make_0_idx, map(int, input().split()))

        for i in range(N):
            for j in range(N):
                for k in range(1,6):
                    visited[i][j][k] = INF
        q = []
        min_visited = INF

        visited[sr][sc][1] = 0
        heapq.heappush(q, (0, -1, sr, sc))

        while q:
            cnt, rev_ck, cr, cc = heapq.heappop(q)
            ck = - rev_ck

            if cnt > visited[cr][cc][ck]:
                continue


            if cr == er and cc == ec:
                min_visited = cnt
                break


            for dr, dc in MOVE:
                # 해당 방향으로 이동하면서, 착지 가능한 좌표에 해당하는 점프량을 반환
                k_list = find_jump_k(cr, cc, dr, dc)
                # print()
                for nk in k_list:
                    # 점프력 증가
                    if ck < nk:
                        n_cnt = cnt
                        for _k in range(ck+1, nk+1):
                            n_cnt += _k**2
                    # 점프력 감소
                    elif ck > nk:
                        n_cnt = cnt + 1
                    # 점프력 동일
                    else:
                        n_cnt = cnt

                    # q push 여부 판단
                    nr, nc = dr*nk+cr, dc*nk+cc
                    if n_cnt+1 < visited[nr][nc][nk]:
                        visited[nr][nc][nk] = n_cnt+1
                        heapq.heappush(q, (n_cnt+1, -nk, nr, nc))

        min_visited = min(min_visited, min(visited[er][ec]))
        answer.append( min_visited if min_visited!=INF else -1  )
        # debug_q()
        # print()
    print('\n'.join(map(str, answer)))

main()