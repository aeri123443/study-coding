'''

개구리의 여행: 2025 상반기 오전 2번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/frog-journey

다시 풀어보기!
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

def append_q(nr, nc, nk, n_cnt):
    if is_range(nr,nc) and n_cnt < visited[nr][nc][nk]:
        visited[nr][nc][nk] = n_cnt
        heapq.heappush(q, (n_cnt, -nk, nr, nc))
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

            ### 점프력 1 증가
            if ck < 5:
                nk = ck+1
                n_cnt = cnt + (nk**2)
                append_q(cr, cc, nk, n_cnt)

            ### 점프량 1~k-1 감소
            if ck != 1:
                for nk in range(ck-1, 0, -1):
                    append_q(cr, cc, nk, cnt+1)

            for dr, dc in MOVE:
                nr, nc = dr*ck+cr, dc*ck+cc

                if not is_range(nr,nc): continue

                # 도착지가 미끄럽거나 천적이 있으면 안 됨
                if board[nr][nc] in ('S', '#'):
                    continue

                # 경로에 천적이 있으면 안 됨
                blocked = False
                for step in range(1, ck):
                    tr, tc = dr*step+cr, dc*step+cc
                    if board[tr][tc] == '#':
                        blocked = True
                        break
                if blocked:
                    continue

                append_q(nr, nc, ck, cnt + 1)


        min_visited = min(min_visited, min(visited[er][ec]))
        answer.append( min_visited if min_visited!=INF else -1  )
        # debug_q()
        # print()
    print('\n'.join(map(str, answer)))

main()