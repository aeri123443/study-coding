'''
고대 문명 유적 탐사: 2024 상반기 오전 1번 문제
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/ancient-ruin-exploration/description

문제 분석: 15m 26s
코드 작성: 2h 18m
디버깅: 16m 22s

총 소요 시간: 2h 50m
'''
from collections import deque
from pprint import pprint
############################################
#### 전역 관리
############################################

N = 5
K, M = 0, 0
INF = float('inf')
CENTER_POS = [
    (1,1), (1,2), (1,3),
    (2,1), (2,2), (2,3),
    (3,1), (3,2), (3,3),
]
MOVE = [(0,1), (1,0), (0,-1), (-1,0)] # 오른쪽, 아래쪽, 왼쪽, 위로

############################################
#### 함수 선언
############################################

# 90도 회전
def rotate(board, center_i, center_j):
    left, right = center_j-1, center_j+1
    top, bottom = center_i-1, center_i+1

    new_rotate = []
    # print(list(zip(*board[top:bottom+1])))
    for z in list(zip(*board[top:bottom+1]))[left:right+1]:
        z = z[::-1]
        new_rotate.append(z)

    for i in range(3):
        ni = i + top
        for j in range(3):
            nj = j + left
            board[ni][nj] = new_rotate[i][j]

# 특정 유물에 대해 인접한 동일 유물 좌표를 반환
def bfs_group(board, visited, si, sj):
    pos = []
    num = board[si][sj]

    q = deque( [(si, sj)] )
    visited[si][sj] = True
    pos.append( (si,sj) )

    while q:
        ci, cj = q.popleft()

        for di, dj in MOVE:
            ni, nj = ci + di, cj + dj

            # 이동 가능, 미방문, 같은 유물
            if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and board[ni][nj]==num:
                visited[ni][nj] = True
                pos.append( (ni,nj) )
                q.append( (ni,nj) )

    return pos

# 3*3 최적의 중심 좌표, 회전 각도, 사라질 유물 좌표 찾기
def find_best_rotate(board):
    best_score = -INF
    best_pos = (INF, INF)
    best_r = INF
    remove_list = []

    for (center_i, center_j) in CENTER_POS:
        # 90도씩 3번 회전 (원상복귀)
        for r in range(3):
            # 회전
            rotate(board, center_i, center_j)

            # 1차 획득 가치 찾기
            tmp_score = 0
            tmp_pos = []

            visited = [[False]*N for _ in range(N)]

            for si in range(N):
                for sj in range(N):
                    # 방문하지 않은 좌표에 대해 bfs 진행
                    if not visited[si][sj]:
                        group_pos = bfs_group(board, visited, si, sj)
                        # 3개 이상의 유물이 인접해있으면 현 회전에 대한 가치 및 좌표 업데이트
                        if len(group_pos) >= 3:
                            tmp_score += len(group_pos)
                            tmp_pos.extend(group_pos)
            # 현 회전에 대한 bfs가 끝나면, score 업데이트
            # 기준: 최고 가치, 최소 각도, 최소 중심c, 최소 중심r
            if (-best_score, best_r, best_pos[1], best_pos[0]) > ( -tmp_score, r, center_j, center_i ):
                best_score = len(tmp_pos)
                best_r = r
                best_pos = (center_i, center_j)
                remove_list = tmp_pos

        # 원상복귀용 회전
        rotate(board, center_i, center_j)

    return {
        'r': best_r,
        'center': best_pos,
        'score': best_score,
        'remove_list': remove_list
    }

# 유물 제거
def remove_item(board, remove_list):
    for i, j in remove_list:
        board[i][j] = 0

# 조각 생성
def create_block(board, create_list, removed_list):
    sorted_removed = sorted(removed_list, key=lambda x: (x[1], -x[0]))
    for i, j in sorted_removed:
        if not create_list : return
        v = create_list.popleft()
        board[i][j] = v
############################################
#### 메인 로직
############################################

def main():
    global K, M

    # 데이터 입력
    K, M = map(int, input().split())
    board = [ list(map(int, input().split())) for _ in range(N)]
    create_list = deque( map(int, input().split())  )
    # K 반복
    for k in range(K):
        # 점수 초기화
        score = 0

        # 3*3 최적의 중심 좌표, 회전 각도, 사라질 유물 좌표 찾기
        best_rotate = find_best_rotate(board)

        # 마땅한 좌표가 없으면 탐색을 종료
        if best_rotate['score'] < 0:
            return
        
        # 유물 1차 획득 (회전 후, 제거 및 점수 업데이트)
        center_i, center_j = best_rotate['center']
        for _ in range(best_rotate['r']+1):
            rotate(board, center_i, center_j)

        remove_item(board, best_rotate['remove_list'])
        score += best_rotate['score']

        # 연쇄 획득
        remove_list = best_rotate['remove_list']
        while True:
            # 조각 생성
            create_block(board, create_list, remove_list)
            # print()
            # 3개 그룹 찾기 (향후 이것도 함수화)
            tmp_score = 0
            tmp_pos = []
            visited = [[False]*N for _ in range(N)]

            for si in range(N):
                for sj in range(N):
                    # 방문하지 않은 좌표에 대해 bfs 진행
                    if not visited[si][sj]:
                        group_pos = bfs_group(board, visited, si, sj)
                        # 3개 이상의 유물이 인접해있으면 가치 및 좌표 업데이트
                        if len(group_pos) >= 3:
                            tmp_score += len(group_pos)
                            tmp_pos.extend(group_pos)

            # 그룹이 더 없으면 종료
            if tmp_score == 0:
                if score > 0:
                    print(score, end=' ')
                    break
                else:
                    return

            # 획득(제거) 및 점수 업데이트
            remove_item(board, tmp_pos)
            remove_list = tmp_pos
            score += tmp_score
            # print()
            # break
        # 점수(획득한 유물 수) 출력

if __name__ == '__main__':
    main()