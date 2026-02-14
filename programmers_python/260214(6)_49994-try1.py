'''
49994. Lv. 2 방문 길이
https://school.programmers.co.kr/learn/courses/30/lessons/49994
30m 5s
'''

'''
캐릭터가 처음 걸어본 길의 길이
좌표평면의 경계를 넘어가는 명령어는 무시
'''
from pprint import pprint
def solution(dirs):
    # UDRL 방문 배열 관리 (어디로 가는지를 포함)
    N = 11
    idx = {'U':0, 'D':1, 'R':2, 'L':3 }
    rev = {'U':'D', 'D':'U', 'R':'L', 'L':'R' } # 반대 방향도 생각
    visited = [[[0,0,0,0] for _ in range(N)] for _ in range(N)]
    move = {'U':(-1,0), 'D':(1,0), 'R':(0,1), 'L':(0,-1) }
    
    ci, cj = 5,5
    answer = 0
    for cmd in dirs:
        # 같은 방향으로 간 적이 있으면 패스
        di, dj = move[cmd]
        ni, nj =  ci+di, cj+dj
        if 0<=ni<N and 0<=nj<N:

            # 저번에 써먹은 길이 아니면!
            if not visited[ci][cj][idx[cmd]]:
                visited[ni][nj][idx[rev[cmd]]] = 1
                visited[ci][cj][idx[cmd]] = 1
                # print(ci, cj, '>', ni, nj)
                answer += 1
            ci, cj = ni, nj
        # print(cmd)
        # pprint(visited)
        # print()
    return answer

print()
print(solution("ULURRDLLU"))
print(7)

print()
print(solution("LULLLLLLU"))
print(7)

print()
print(solution("LRLRLRLRLR"))
print(1)

# print()
# print(solution())
# print()