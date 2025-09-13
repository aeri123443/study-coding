'''
p.502 50. N-퀸
https://school.programmers.co.kr/learn/courses/30/lessons/12952
소요시간: 81m 35s 
'''
import pprint

def dfs(n, i):
    global y_set, board, answer
    for j in range(n):
        # print(i, j, c1_set)
        if (j not in y_set) and (n-i-j not in c1_set) and (i-j not in c2_set):
            if i==n-1:
                board[i][j] = 'O'
                # pprint.pprint(board)
                answer += 1
                board[i][j] = 'X'
            else:
                board[i][j] = 'O'
                y_set.add(j)
                c1_set.add(n-i-j)
                c2_set.add(i-j)
                dfs(n, i+1)
                board[i][j] = 'X'
                y_set.remove(j)
                c1_set.remove(n-i-j)
                c2_set.remove(i-j)    

def solution(n):
    global answer, x_set, y_set, c1_set, c2_set, board
    answer = 0
    x_set, y_set, c1_set, c2_set = set(), set(), set(), set()
    board = [['X']*n for _ in range(n)]

    dfs(n, 0)
    return answer

# 2
# print(solution(4))
print(solution(5))

