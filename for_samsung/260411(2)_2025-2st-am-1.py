'''

왕실의 기사 대결:  2025 하반기 오전 1번 문제
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/delivery-service/description

문제 분석: 18m 25s
코드 작성: 2h 14m 49s
디버깅: 0s

총 소요 시간: 2h 33m 14s
'''


###################################
#### 모듈 선언 및 전역 관리
###################################
from collections import defaultdict

N, M = -1, -1
MAX_K = -1
###################################
#### 함수 선언
###################################

# 중력 적용 - 리팩토링: 나중에 삭제 가능성 있음
def gravity(board, items, k):

    row, col, w, h = items[k]

    sj, ej = col, col+w-1

    floor = row

    # 떨어질 row 위치 찾기
    for r in range(row, N-1):
        # 다음 행이 모두 비어있으면
        flag = True
        for c in range(sj, ej+1):
            if board[r+1][c] != -1:
                flag = False
                break
        if flag:
            floor = r+1
        else:
            break

    si, ei = floor-h+1, floor
    items[k][0] = si

    # 택배 놓기
    for i in range(si, ei+1):
        for j in range(sj, ej+1):
            board[i][j] = k

    # print()


        # floor +1
        # 아니먄 break

# 택배 투입
def input_items(board, items):
    global MAX_K

    for _ in range(M):
        k, h, w, c = map(int, input().split())
        c -= 1 # 0 좌표 보정
        items[k] = [0, c, w, h] # 현재 r, 현재 c, w, h
        gravity(board, items, k)
        MAX_K = max(MAX_K, k)

# 제거할 상품 찾기
# +1: 왼쪽->오른쪽 탐색(왼쪽 하차), -1: 오른쪽 -> 왼쪽 탐색 (오른쪽 하차)
def find_remove_item(board, items, dj):
    side_cnt = defaultdict(int) # 사이드에 있는 아이템들을 저장

    for i in range(N):
        # 가로행 탐색 중 아이템 나오면 바로 종료
        j = 0 if dj == +1 else N - 1
        while 0 <= j < N:
            if board[i][j] != -1:
                side_cnt[ board[i][j] ] += 1
                break
            j += dj

    # item 탐색
    for idx in range(MAX_K+1):
        # items에 존재하지 않으면 넘어감
        if idx not in items: continue
        # side_cnt에 존재하지 않으면 넘어감
        if idx not in side_cnt: continue

        # side_cnt의 값과 h값이 일치해야 함!
        if side_cnt[idx] == items[idx][3]:
            return idx

    # print()
    return -1

# 상품 제거하기 (하차)
def remove_item(board, items, removed_item):
    r, c, w, h = items[removed_item]
    si, ei = r, r+h-1
    sj, ej = c, c+w-1

    # 보드에서 지우고
    for i in range(si, ei+1):
        for j in range(sj, ej+1):
            board[i][j] = -1

    # items 목록에서도 제거
    del items[removed_item]

    # 사라진 아이템의 열 정보를 반환 (향후 중력 적용을 위함)
    return sj, ej

# 하강 가능한 아이템 후보 찾기
# 사라진 아이템의 열 좌표를 기준으로 탐색 -> 그냥 맨 밑에 있는거 다 반환
# 리팩토링: 나중에 gravity 함수랑 합치기
def find_down_candidate(board, sj, ej):
    candidate_arr = []
    candidate_set = set()

    for i in range(N):
        # for j in range(sj, ej+1):
        for j in range(N):
            if board[i][j] != -1 and board[i][j] not in candidate_set:
                candidate_set.add(board[i][j])
                candidate_arr.append(board[i][j])
    return candidate_arr

# 중력 적용 (적용 가능한지 확인 후 하강)
def down_items(board, down_candidate, items):
    while down_candidate:
        k = down_candidate.pop()
        r, c, w, h = items[k]
        si, ei = r, r+h-1
        sj, ej = c, c+w-1

        # 상품의 바닥을 기준으로
        # 다음 행이 비어있는지 확인
        floor = ei
        for i in range(floor+1, N):
            flag = True
            for j in range(sj, ej+1):
                if board[i][j] != -1:
                    flag = False
                    break
            # floor 업데이트
            if flag: floor += 1
            else: break

        # floor에 변화가 있으면 하강을 진행
        if floor != ei:

            # 전체적으로 한 번 지우고
            for i in range(si,ei+1):
                for j in range(sj, ej+1):
                    board[i][j] = -1

            # 다시 채워넣기
            si, ei = floor - h + 1, floor
            for i in range(si,ei+1):
                for j in range(sj, ej+1):
                    board[i][j] = k

            # items에도 상태 업데이트
            items[k] = [si, sj, w, h]

###################################
#### 메인 로직
###################################
def main():
    global N, M
    N, M = map(int, input().split())
    board = [ [-1]*N for _ in range(N) ]
    items = defaultdict(list) # 현재 r, 현재 c, w, h
    answers = []
    # 택배 투입
    input_items(board, items)

    # 택배 사라질 때까지
    dj = +1 # -1 곱하며 과정을 반복
    while items:
        # 왼/오른쪽에서 뺄 상품 찾기
        removed_item = find_remove_item(board, items, dj)
        # 왼/오른쪽 하차
        rm_sj, rm_ej = remove_item(board, items, removed_item)
        # 중력 적용 후보 탐색 (사라진 열에 있는 모든 아이템을 반환 -> (수정) 그냥 다 반환)
        down_candidate = find_down_candidate(board, rm_sj, rm_ej)
        # 중력 적용 (적용 가능한지 확인 후 하강)
        down_items(board, down_candidate, items)
        # 제거 아이템 추가
        answers.append(removed_item)
        dj *= -1
        # print()
    print( '\n'.join( map(str, answers)))


if __name__ == '__main__':
    main()