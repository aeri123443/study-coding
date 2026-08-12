'''
고대 문명 유적 탐사: 2024 상반기 오전 1번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/ancient-ruin-exploration

문제 분석: 11m 31s
코드 작성: 1h 20m 27s
최종 디버깅: 0m 0s

총 소요 시간: 1h 31m 58s
'''

from collections import deque
# =============================================
# 전역 선언
# =============================================

N = 5
K, M = -1, -1

INF = float('inf')
MOVE = [(+1,0), (-1,0), (0,+1), (0,-1)]
S_LIST = [(i, j) for i in range(3) for j in range(3)] # 3*3 시작점 표

board = []
m_list = deque()

# =============================================
# 보조 함수
# =============================================

# 초기 데이터 입력
def input_data():
    global K, M, board, m_list

    M, K = map(int, input().split())
    board = [list(map(int,input().split())) for _ in range(N)]
    m_list.extend(map(int,input().split()))

# 90도 회전
def rotate(sr, sc):
    er, ec = sr+3, sc+3

    tmp_area = []
    for r in range(sr, er):
        tmp_line = []
        for c in range(sc, ec):
            tmp_line.append(board[r][c])
        tmp_area.append(tmp_line)

    # 열을 행의 역순으로 넣음
    for i in range(3):
        for j in range(3):
            board[j+sr][2-i+sc] = tmp_area[i][j] # (i,j) -> (j,N-1-i) + (sr,sc)
    # print()

def bfs(sr, sc, visited):
    q = deque([(sr, sc)])
    visited[sr][sc] = True
    num = board[sr][sc]
    same_list = [(sr,sc)]

    while q:
        cr, cc = q.popleft()

        for dr, dc in MOVE:
            nr, nc = dr+cr, dc+cc
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and board[nr][nc]==num:
                same_list.append((nr,nc))
                visited[nr][nc] = True
                q.append((nr,nc))

    return same_list

# 획득 가능한 유물 리스트
def find_remove_items():
    ans = []
    visited = [[False]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                same_list = bfs(i,j, visited)
                if len(same_list) >= 3:
                    ans.extend(same_list)
    return ans

# 디버깅: 보드 확인용 프린트
def debug_board(r, sr, sc):
    print(f'회전:{r}, sr:{sr}, sc:{sc}')
    for i in range(N):
        print(' '.join(map(str, board[i])))
# =============================================
# 메인 로직
# =============================================
def main():
    # =====================
    # 0. 초기 데이터 입력
    # =====================
    input_data()
    # print()

    answer = []
    for _ in range(M):
        get_cnt = 0

        # =====================
        # 1. 탐사 진행
        # =====================
        # 최다 획득 가치, 최소 회전, 최소c, 최소r
        explore_info = (-INF, -INF, -INF, -INF)

        # 중심축 기준으로 90, 180, 270도 회전
        # debug_board()
        for sr, sc in S_LIST:
            for r in range(3):
                # 90도 회전
                rotate(sr, sc)
                # debug_board(r, sr, sc)
                # 획득 가능한 유물 리스트
                same_list = find_remove_items()
                explore_info = max(explore_info, (len(same_list), -r, -sc, -sr))
            rotate(sr, sc) # 회전 원상복귀

        val, rev_r, rev_sc, rev_sr = explore_info
        r, sc, sr = -rev_r, -rev_sc, -rev_sr

        # 획득할 유물이 없을 경우 조기 종료
        if val == 0: break

        # 실제 회전 적용
        for _ in range(r+1):
            rotate(sr, sc)
        # print()
        # 유물 연쇄 획득
        while True:
            # 획득할 유물 탐색
            same_list = find_remove_items()
            # print()
            # 유물이 더 없으면 종료
            if not same_list: break

            # 유물 정렬 및 업데이트
            same_list.sort(key=lambda x: (x[1], -x[0]))
            # print()
            for i, j in same_list:
                n = m_list.popleft()
                board[i][j] = n

            # 획득 가치 업데이트
            get_cnt += len(same_list)

        # 최적의 탐사 업데이트
        answer.append(get_cnt)
        # print()
    print(' '.join(map(str, answer)))

main()