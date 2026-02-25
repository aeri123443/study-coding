'''
121687. [PCCP 모의고사 #2] 1번 - 실습용 로봇
https://school.programmers.co.kr/learn/courses/15009/lessons/121687
'''

'''
'R': 로봇이 오른쪽으로 90도 회전합니다.
'L': 로봇이 왼쪽으로 90도 회전합니다.
'G': 로봇이 한 칸 전진합니다.
'B': 로봇이 한 칸 후진합니다.
'''

def solution(command):
    command = list(command)
    move = [(0,+1), (+1,0), (0,-1), (-1,0)]
    move_idx = 0
    x, y = 0,0
    
    for c in command:
        # 'R': 로봇이 오른쪽으로 90도 회전합니다.
        if c == 'R': 
            move_idx += 1
            move_idx %= 4
        # 'L': 로봇이 왼쪽으로 90도 회전합니다.
        elif c == 'L': 
            move_idx -= 1
            move_idx %= 4
        # 'G': 로봇이 한 칸 전진합니다.
        elif c == 'G': 
            x += move[move_idx][0]
            y += move[move_idx][1]   
        # 'B': 로봇이 한 칸 후진합니다.
        else: 
            x -= move[move_idx][0]
            y -= move[move_idx][1]    
        # print(c, move_idx, x, y)
        
    return [x,y]
