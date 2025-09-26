'''
고대 문명 유적 탐사: 2024 상반기 오전 1번 문제 (L12)
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/ancient-ruin-exploration/description
소요시간: 3h 49m

[리뷰]
리스트 하나를 두 리스트에 추가하면안됨!! 슬라이싱 사용하기
연산자 체이닝이 가능한 언어임
행열 구분 똑바로 하기
""탐색을 즉시 종료합니다"" 놓치지 말것
answer가 0이 아닐 때 뭘 하는 건 좋았는데, '그럼 0이면?'도 생각했어야 함
'''

import sys
from pprint import pprint
sys.stdin = open('input.txt', 'r')

N = 5 # 맵 행/열 길이
center_list = [[1,1], [1,2], [1,3], [2,1], [2,2], [2,3], [3,1], [3,2], [3,3]] # 격자 중심
K, M = map(int, input().split())
default_map = [] # 초기 맵
temp_map = [] # 회전 때마다 사용할 임시 맵
M_list = [] # 벽면 조각 리스트
M_idx = 0 # 큐 대신 활용
visited = [[False] * N for _ in range(N)]
move = [[1,0], [-1,0], [0,1], [0,-1]]
same_num = [] # 그룹찾기 시 활용
answer = 0

#### 데이터 입력 및 초기화 ####

### 데이터 입력
def input_data():
    global default_map, temp_map, M_list, M, N

    ## 맵 입력
    for _ in range(N):
        lst = list(map(int, input().split()))
        default_map.append(lst[:])
        temp_map.append(lst[:])

    ## 유물 조각 리스트 입력
    M_list = list(map(int, input().split()))

### visited 초기화
def init_visited():
    global visited, N
    for i in range(N):
        for j in range(N):
            visited[i][j] = False

#### 1단계: 회전 ####

### 격자 90도 회전
def rotate(ci, cj, r, target='t'):
    global default_map, temp_map
    di, dj = ci - 1, cj - 1

    if target == 't':
        # (1,1) 센터 기준으로 임시 좌표로 변환 후 di,dj 붙이기
        if r==90:
            for i in range(3):
                for j in range(3):
                    temp_map[j+di][3-i-1+dj] = default_map[i+di][j+dj]
        elif r==180:
            for i in range(3):
                for j in range(3):
                    temp_map[3-i-1+di][3-j-1+dj] = default_map[i+di][j+dj]
        elif r==270:
            for i in range(3):
                for j in range(3):
                    temp_map[3-j-1+di][i+dj] = default_map[i+di][j+dj]
        elif r==0: ## 되돌리기
            for i in range(3):
                for j in range(3):
                    temp_map[i+di][j+dj] = default_map[i+di][j+dj]

    elif target == 'd':
        if r == 90:
            for i in range(3):
                for j in range(3):
                    default_map[j + di][3 - i - 1 + dj] = temp_map[i + di][j + dj]
        elif r == 180:
            for i in range(3):
                for j in range(3):
                    default_map[3 - i - 1 + di][3 - j - 1 + dj] = temp_map[i + di][j + dj]
        elif r == 270:
            for i in range(3):
                for j in range(3):
                    default_map[3 - j - 1 + di][i + dj] = temp_map[i + di][j + dj]
        # temp_map을 동기화시킴
        for i in range(3):
            for j in range(3):
                temp_map[i + di][j + dj] = default_map[i + di][j + dj]

    # 업데이트
    # for i in range(ci-1, ci+2):
    #     for j in range(cj-1, cj+2):
    #         default_map[i][j] = temp_map[i][j]

### 그룹 찾는 dfs
def dfs_group(si, sj, num):
    global temp_map, visited, N, move, same_num

    for di, dj in move:
        ni, nj = di+si, dj+sj
        # 다음좌표가 방문 가능한 좌표 + 같은 유적조각이면
        if N > ni >= 0 and N > nj >= 0 and visited[ni][nj]==False and temp_map[ni][nj]==num:
            visited[ni][nj] = True
            same_num.append([ni, nj])
            dfs_group(ni, nj, num)

    # 계속 탐색

### 그룹 찾기
def group():
    global temp_map, visited, M_list, same_num, N

    # 조각 개수, 각 유물 위치
    tmp_info = [0, []]
    init_visited()

    # 방문 안 한 좌표를 찾고
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            same_num = [[i, j]]
            visited[i][j] = True
            # print(i, j, default_map[i][j])
            dfs_group(i, j, temp_map[i][j])
            # 개별 그룹 크기가 3 이상이라면, 점수와 인포 반환
            # print(same_num)
            if len(same_num) >= 3:
                tmp_info[0]+=len(same_num)
                tmp_info[1].extend(same_num)
    # pprint(tmp_info)
    return tmp_info

### 최적의 회전값 찾기
def find_best_rotate():
    global default_map, center_list, temp_map
    
    # 획득 조각 수, 각도, 중심열, 중심행, 유물 좌표들
    max_info = [0, float('inf'), float('inf'), float('inf'), []]

    # center_list = [[2,2]]
    # 격자에 따라 9번 반복 3회씩 회전
    for ci, cj in center_list:
        # print(ci, cj)
        for r in [90, 180, 270]: # 90도, 180도, 270도 회전
            rotate(ci, cj, r)
            # pprint(temp_map)

            # 그룹 찾고 점수 max_info 업데이트
            tmp_info = group()
            max_info = max(max_info, [tmp_info[0], r, ci, cj, tmp_info[1]], key=lambda x: (x[0], -x[1], -x[3], -x[2]))
            # pprint('tmp_info')
            # pprint(tmp_info)
            # pprint('max_info')
            # pprint(max_info)

        # 초기 회전 상태로
        rotate(ci, cj, 0)

    return max_info

### 조각 교체
def replace_m(max_list):
    global default_map, temp_map, M_list, M_idx, N

    max_list.sort(key=lambda x: (x[1], -x[0]))
    # print(max_list)
    for i, j in max_list:
        default_map[i][j] = M_list[M_idx]
        temp_map[i][j] = M_list[M_idx]
        M_idx += 1
    # print(M_idx)
    # pprint(default_map)

#### 유물 연쇄 획득 ####

### 유물 연쇄 획득
def get_more():
    global default_map, answer
    # 유물이 더 없을 때까지 반복
    while True:
        # 그룹 찾기
        tmp_score, temp_list = group()

        if tmp_score == 0: break

        # 점수 계산 및 유물 조각 교체
        answer += tmp_score
        replace_m(temp_list)

#### main ####

### 데이터 입력, 필요 맵 생성
input_data()
# pprint(default_map)
# pprint(temp_map)
# pprint(M_list)


# for _ in range(1):
for _ in range(K):
    answer = 0
    # print('')
    # print(k)

    ### 회전

    # 최적의 회전 결과값 찾기   
    max_num, max_rotate, max_ci, max_cj, max_list = find_best_rotate()

    # pprint(default_map)
    # print(max_num, max_rotate, max_ci, max_cj, max_list)
    # 결과값 기반으로 디폴트맵 회전 및 유물 정보
    answer += max_num
    rotate(max_ci, max_cj, max_rotate, target='d')
    # pprint(default_map)
    ### 조각 교체
    replace_m(max_list)
    # pprint('replace_m...')
    # pprint(default_map)

    ### 유물 연쇄 획득
    get_more()
    # print('M_', M_idx, M_list)
    # pprint(default_map)

    if answer > 0:
        # print('answer:', answer)
        print(answer, end=' ')
    else:
        break
