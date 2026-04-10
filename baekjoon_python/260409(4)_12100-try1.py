'''
12100. <골드 1> 2048 (Easy)
https://www.acmicpc.net/problem/12100

문제 읽고 코드 작성: 1h 15m 45s
디버깅: 14m 25s

총 풀이 시간: 1h 30m 10s
'''
from itertools import product
from collections import deque

##########################
#### 전역 선언
##########################
N = 0

##########################
#### 함수 선언
##########################

# 왼쪽
def move_left(board):
    for i in range(N):
        stack = [] # (값, 합쳐짐 여부)

        for j in range(N):
            if board[i][j] == 0:
                continue
            else:
                # 스택의 최근 값이 합쳐지지 않았고(false), 최근 값과 지금 값이 같으면 합침
                if stack and not stack[-1][1] and board[i][j] == stack[-1][0]:
                    stack[-1] = ( stack[-1][0]*2,  True)
                else:
                    stack.append( (board[i][j], False) )

        # board 업데이트
        stack.extend( [(0, False)]*(N-len(stack)) )
        for j in range(N):
            board[i][j] = stack[j][0]

# 오른쪽
def move_right(board):
    for i in range(N):
        q = deque() # (값, 합쳐짐 여부)

        for j in range(N-1, -1, -1):
            if board[i][j] == 0:
                continue
            else:
                if q and not q[0][1] and board[i][j] == q[0][0]:
                    q[0] = ( q[0][0]*2,  True)
                else:
                    q.appendleft( (board[i][j], False) )

        q.extendleft( [(0, False)]*(N-len(q)) )
        for j in range(N):
            board[i][j] = q[j][0]

# 위쪽
def move_up(board):
    for j in range(N):
        stack = [] # (값, 합쳐짐 여부)

        for i in range(N):
            if board[i][j] == 0:
                continue
            else:
                # 스택의 최근 값이 합쳐지지 않았고(false), 최근 값과 지금 값이 같으면 합침
                if stack and not stack[-1][1] and board[i][j] == stack[-1][0]:
                    stack[-1] = ( stack[-1][0]*2,  True)
                else:
                    stack.append( (board[i][j], False) )
        # print()
        # board 업데이트
        stack.extend( [(0, False)]*(N-len(stack)) )
        for i in range(N):
            board[i][j] = stack[i][0]

# 아래쪽
def move_down(board):
    for j in range(N):
        q = deque() # (값, 합쳐짐 여부)

        for i in range(N-1, -1, -1):
            if board[i][j] == 0:
                continue
            else:
                if q and not q[0][1] and board[i][j] == q[0][0]:
                    q[0] = ( q[0][0]*2,  True)
                else:
                    q.appendleft( (board[i][j], False) )

        # board 업데이트
        q.extendleft( [(0, False)]*(N-len(q)) )
        for i in range(N):
            board[i][j] = q[i][0]

# 가장 큰 값 찾기
def find_max(board):
    m = -1
    for i in range(N):
        m = max(m, max(board[i]))
    return m
##########################
#### 메인 로직
##########################
def main():
    global N
    max_num = -1

    # 값 입력
    N = int(input())
    input_board = [ list(map(int, input().split())) for _ in range(N) ]

    # 5회 이동하는 경우의 수 생성
    moving_list = product(['l', 'r', 'u', 'd'], repeat=5)

    # 5회씩 반복
    for cmd in moving_list:
        # 새 보드 생성
        board = []
        for i in range(N):
            board.append(input_board[i][:])
        # print()
        for c in cmd:
            if c == 'l':
                move_left(board)
            elif c == 'r':
                move_right(board)
            elif c == 'u':
                move_up(board)
            else: # c == 'd'
                move_down(board)

        # 가장 큰 값 업데이트
        max_num = max(max_num, find_max(board))

    print(max_num)

main()