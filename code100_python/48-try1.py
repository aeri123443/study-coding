'''
p.488 48. 스토쿠 퍼즐
'''

import pprint

# 동일 열
def in_col(board, col_num, target):
    return target in board[col_num]
# 동일 행
def in_row(board, row_num, target):
    for i in range(len(board)):
        if board[i][row_num]==target:
            return True
    return False
# 동일 박스
def in_box(board, x,y, target):
    mapping = {
        0: [0,1,2], 1: [0,1,2], 2: [0,1,2],
        3: [3,4,5], 4: [3,4,5], 5: [3,4,5],
        6: [6,7,8], 7: [6,7,8], 8: [6,7,8],
    }

    x_map, y_map = mapping[x], mapping[y]
    for _y in y_map:
        for _x in x_map:
            # print(_x, _y, board[_x][_y], target)
            if board[_x][_y]==target:
                # print(target, 'is in', _x, _y)
                return True
    return False
# 유효성 검사
def is_balid(board, target, x, y):
    if in_col(board, x, target): 
        return False
    if in_row(board, y, target): 
        return False
    if in_box(board, x,y, target):
        return False
    return True
# 스토쿠 dfs
def dfs(board, empty_arrs, N):
    # print(empty_arrs)
    # time.sleep(0.5)
    if len(empty_arrs)>0:
        x,y = empty_arrs.pop()
        # print(x,y)
        for i in range(1, N+1):
            if is_balid(board, i, x, y):
                board[x][y]=i
                # print(x, y, 'is', i)
                result = dfs(board, empty_arrs, N)
                if result==False:
                    board[x][y]=0
                    # print(x, y, 'is not', i)
                else: return
        if len(empty_arrs)==0:
            return
        empty_arrs.append([x,y])
        return False
    

    # 재귀로 유효성 검사하고 넣고 다음단계로
    # 안 맞으면 0으로 돌림
def solution(board):
    N = len(board)
    # 빈 배열들 찾고 반환
    empty_arrs = []
    for i in range(N):
        for j in range(N):
            if board[i][j]==0:
                empty_arrs.append([i, j])
    # print(empty_arrs)
    dfs(board, empty_arrs, N)
    return board


pprint.pprint(solution(
    [
      [5, 3, 0, 0, 7, 0, 0, 0, 0],
      [6, 0, 0, 1, 9, 5, 0, 0, 0],
      [0, 9, 8, 0, 0, 0, 0, 6, 0],
      [8, 0, 0, 0, 6, 0, 0, 0, 3],
      [4, 0, 0, 8, 0, 3, 0, 0, 1],
      [7, 0, 0, 0, 2, 0, 0, 0, 6],
      [0, 6, 0, 0, 0, 0, 2, 8, 0],
      [0, 0, 0, 4, 1, 9, 0, 0, 5],
      [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
))

# print(solution(
#     [
#         [0,0,0],
#         [0,0,0],
#         [0,0,0]
#     ]
# ))

# print(solution(
#     [
#         [1,0,2],
#         [0,2,0],
#         [2,1,3]
#     ]
# ))

# print(solution(
#     [
#         [1,0,2],
#         [0,2,0],
#         [2,0,0]
#     ]
# ))

# pprint.pprint(solution(
#     [
#       [0, 0, 0, 0, 0, 0, 0, 0, 0],
#       [0, 0, 0, 0, 0, 0, 0, 0, 0],
#       [0, 0, 0, 0, 0, 0, 0, 0, 0],
#       [0, 0, 0, 0, 0, 0, 0, 0, 0],
#       [0, 0, 0, 0, 0, 0, 0, 0, 0],
#       [0, 0, 0, 0, 0, 0, 0, 0, 0],
#       [0, 0, 0, 0, 0, 0, 0, 0, 0],
#       [0, 0, 0, 0, 0, 0, 0, 0, 0],
#       [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     ]
# ))
