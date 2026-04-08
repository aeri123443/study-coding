'''
17406. <골드 4> 배열 돌리기 4
https://www.acmicpc.net/problem/17406

문제 읽고 분석: 12m 54s
코드 작성: 1h 00m 48s
디버깅: 0s

총 풀이 시간: 1h 13m 42s

리뷰: 회전 템플릿!!
'''
from itertools import permutations

#########################
#### 전역변수 선언
#########################

N, M, K = map(int, input().split())

input_board = [ list(map(int, input().split())) for _ in range(N) ]
input_rotate = [tuple(map(int, input().split())) for _ in range(K)]

min_answer = float('inf')

#########################
#### 함수 선언
#########################

# rotate: 회전 연산에 따른 회전을 수행
# 회전 결과 보드를 리턴
def rotate( prev_board, r, c, s ):
    r_idx, c_idx = r-1, c-1

    # 깊은 복사
    new_board = []
    for i in range(N):
        row = prev_board[i][::]
        new_board.append(row)

    # s값을 1부터 증가시키며 회전 연산을 수행
    for _s in range(1, s+1):
        min_r, max_r = r_idx - _s, r_idx + _s
        min_c, max_c = c_idx - _s, c_idx + _s

        # ro_list: 회전 순서를 담은 리스트
        ro_list = []

        # 좌측상단부터 하나씩 리스트에 담고 (첫 데이터는 한 번 더 넣기)
        for _c in range(min_c, max_c):
            ro_list.append( (min_r, _c) )
        for _r in range(min_r, max_r+1):
            ro_list.append( (_r, max_c) )
        for _c in range(max_c-1, min_c-1, -1):
            ro_list.append( (max_r, _c) )
        for _r in range(max_r-1, min_r-1, -1): # 마지막 값 한 번 더 포함
            ro_list.append( (_r, min_c) )
        # print('ro_list: ', ro_list)

        # 리스트에 따라 값 이동
        for i in range(len(ro_list)-1):
            cur_r, cur_c = ro_list[i]
            nxt_r, nxt_c = ro_list[i+1]
            new_board[nxt_r][nxt_c] = prev_board[cur_r][cur_c]

    return new_board


# 배열 A의 값 구하기
# 배열 A의 값은 각 행에 있는 모든 수의 합 중 최솟값
def find_a(board):
    min_result = float('inf')

    for i in range(N):
        sum_row = sum(board[i])
        min_result = min(min_result, sum_row)

    return min_result

#########################
#### 메인 로직
#########################

# 회전연산 경우의 수만큼 반복
for rotate_arr in permutations(input_rotate):

    # 회전 연산대로 배열 회전 -> 회전 결과를 리턴

    rotated_board = []

    for i in range(N): # 깊은 복사
        row = input_board[i][::]
        rotated_board.append(row)

    for (r, c, s) in rotate_arr:
        rotated_board = rotate(rotated_board, r, c, s)
        # print()

    # '배열 A의 값' 구하기
    value_a = find_a(rotated_board)

    # 최솟값 업데이트
    min_answer = min(value_a, min_answer)

print(min_answer)