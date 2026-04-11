def gravity_line(line, n):
    stack = []
    for v in line:
        if v > 0:
            stack.append(v)

    stack.extend( [0]*(n-len(stack)) )

    return stack

def apply_gravity(board, n, d):
    new_board = [ [0]*n for _ in range(n)]

    if d==0: # left
        for i in range(n):
            arr = gravity_line(board[i], n)
            new_board[i] = arr
    elif d==1: #up
        for j in range(n):
            line = [board[i][j] for i in range(n)]
            arr = gravity_line(line, n)
            for i in range(n):
                new_board[i][j] = arr[i]
    elif d==2: # right
        for i in range(n):
            line = board[i]
            arr = gravity_line(line[::-1], n)[::-1]
            new_board[i] = arr
    else: # down
        for j in range(n):
            line = [board[i][j] for i in range(n)]
            arr = gravity_line(line[::-1], n)[::-1]
            for i in range(n):
                new_board[i][j] = arr[i]

    return new_board

n = 4
board = [
    [0, 2, 0, 3],
    [2, 0, 2, 4],
    [3, 1, 0, 5],
    [4, 5, 4, 0]
]

# left
print( apply_gravity(board, n, 0) )
# up
print( apply_gravity(board, n, 1) )
# right
print( apply_gravity(board, n, 2) )
# down
print( apply_gravity(board, n, 3) )
