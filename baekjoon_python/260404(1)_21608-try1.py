'''
21608. <골드 5> 상어 초등학교
https://www.acmicpc.net/problem/21608
1h 11m 14s
'''
# from pprint import pprint

## 좋아하는 학생 체크
def find_friends(likes): # 학생 번호, set
    max_cnt = 0
    max_list = []
    # 한 칸씩 돌면서
    # for arr in students:
    #     n, s = arr[0], arr[1] # 학생 번호, set
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0: continue
            # 상하좌우 살펴보기
            tmp_cnt = 0
            for di, dj in move:
                ni, nj = i+di, j+dj
                if 0<=ni<N and 0<=nj<N and board[ni][nj] in likes:
                    # print(i, j, ni, nj)
                    tmp_cnt += 1

            if max_cnt == tmp_cnt:
                max_list.append( (i,j) )
            elif max_cnt < tmp_cnt:
                max_cnt = tmp_cnt
                max_list = [ (i,j) ]

    # print(max_cnt, max_list)
    return max_list

    # 좋아하는 학생이 있는지 체크
    # max, 좌표 업데이트

## 비어있는 칸 체크
def find_empty(like_list):
    max_cnt = 0
    max_list = []

    for i, j in like_list:
            if board[i][j] > 0: continue
            # 상하좌우 살펴보기
            tmp_cnt = 0
            for di, dj in move:
                ni, nj = i+di, j+dj
                if 0<=ni<N and 0<=nj<N and board[ni][nj] == 0:
                    # print(i, j, ni, nj)
                    tmp_cnt += 1

            if max_cnt == tmp_cnt:
                max_list.append( (i,j) )
            elif max_cnt < tmp_cnt:
                max_cnt = tmp_cnt
                max_list = [ (i,j) ]

    # print(max_cnt, max_list)
    return max_list

## r, c 가장 작은 값 반환
def find_min_rc(empty_list):
    # r이 가장 작은 리스트
    min_r = min(empty_list, key=lambda x: x[0])
    min_list = [(i,j) for (i,j) in empty_list if i==min_r[0]]
    if len(min_list) == 1:
        return min_list[0]

    # c가 가장 작은 리스트
    min_c = min(min_list, key=lambda x: x[1])
    return min_c

## 점수 합산 및 반환
def cal_score():
    map_score = [0, 1, 10, 100, 1000]
    score = 0

    # 한 칸씩 돌면서
    for i in range(N):
        for j in range(N):
            n = board[i][j]
            # 상하좌우에 좋아하는 학생 몇명인지 체크
            tmp_num = 0
            for di, dj in move:
                ni, nj = i+di, j+dj
                if 0<=ni<N and 0<=nj<N and board[ni][nj] in s_mapping[n]:
                    tmp_num += 1
            score += map_score[tmp_num]
    print(score)

#### main

## 값 입력
N = int(input())
S_NUM = N*N

students = []
s_mapping = {}
for _ in range(S_NUM):
    tmp = []
    tmp_input = list(map(int, input().split()))

    students.append(tmp_input[0])
    s_mapping[tmp_input[0]] = set(tmp_input[1:])

board = [[0]*N for _ in range(N)]
move = [(0,1), (0,-1), (1,0), (-1,0)]
# for x in students: print(x)

# 학생 하나하나씩 실행하며 자리 배치하기
for n in students:
    likes = s_mapping[n]
    # print('n = ', n)
    # print('likes = ', likes)

    like_list = find_friends(likes)
    # print('  like_list: ', like_list)
    if len(like_list) == 1:
        i, j = like_list[0]
        board[i][j] = n
        # pprint(board)
        continue

    empty_list = find_empty(like_list)
    # print('  empty_list: ', empty_list)
    if len(empty_list) == 1:
        i, j = empty_list[0]
        board[i][j] = n
        # pprint(board)
        continue

    min_rc = find_min_rc(empty_list)
    # print('  min_rc: ', min_rc)
    i, j = min_rc
    board[i][j] = n
    # pprint(board)

# pprint(board)
cal_score()
