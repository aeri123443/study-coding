'''
p.617 69. 캐릭터의 좌표
https://school.programmers.co.kr/learn/courses/30/lessons/120861
소요시간: 9m 47s
'''

def solution(keyinput, board):
    max_x, max_y = board[0]//2, board[1]//2
    min_x, min_y = max_x*-1, max_y*-1
    x, y = 0, 0

    for k in keyinput:
        if k == "right" and x<max_x: x+=1
        elif k == "left" and x>min_x: x-=1
        elif k == "up" and y<max_y: y+=1
        elif k == "down" and y>min_y: y-=1
    return [x,y]

# [2, 1]
print(solution(["left", "right", "up", "right", "right"], [11, 11]))
# [0, -4]
print(solution(["down", "down", "down", "down", "down"], [7, 9]))
