'''
p.326 30. 미로 탈출
https://school.programmers.co.kr/learn/courses/30/lessons/159993
소요시간: 
이전의 코드는 큐에서 뽑은 후 방문처리를 했는데, 이렇게 하면 이 큐를 뽑기 전까지 같은 큐가 쌓여버릴 수도 있음. 
앞으로 가는 놈이랑, 다음 차례에서 뒤로 가는 놈이 겹쳐버리는 셈!
'''

from collections import deque

def solution(maps):
    x_max = len(maps)
    y_max = len(maps[0])

    # S, E, L 찾기
    s, l, e = [], [], []
    for x in range(x_max):
        for y in range(y_max):
            if maps[x][y] == 'S':
                s = [x, y]
            elif maps[x][y] == 'L':
                l = [x, y]
            if maps[x][y] == 'E':
                e = [x, y]

    def issamexy(a,b):
        return a[0]==b[0] and a[1]==b[1]

    def bfs(queue, l, e):
        visited = [[False]*y_max for _ in range(x_max)]
        while queue:
            # print(queue)
            position, visited_laber, cnt = queue.popleft()
            # print(position, visited_laber, cnt)
            [x, y] = position
            # visited[x][y] = True

            # L을 만나면 첫 단계인지 파악
            if issamexy(position, l):
                if not visited_laber:
                    return position, True, cnt
            elif issamexy(position, e):
                if visited_laber:
                    return position, True, cnt
            
            # 좌표 확인 후 큐에 넣기
            if x+1 < x_max and not visited[x+1][y] and maps[x+1][y]!='X':
                visited[x+1][y] = True
                queue.append([[x+1, y], visited_laber, cnt+1])
            if y+1 < y_max and not visited[x][y+1] and maps[x][y+1]!='X':
                visited[x][y+1] = True
                queue.append([[x, y+1], visited_laber, cnt+1])
            if x-1 >= 0 and not visited[x-1][y] and maps[x-1][y]!='X':
                visited[x-1][y] = True
                queue.append([[x-1, y], visited_laber, cnt+1])
            if y-1 >= 0 and not visited[x][y-1] and maps[x][y-1]!='X':
                visited[x][y-1] = True
                queue.append([[x, y-1], visited_laber, cnt+1])

        # 벽을 넘지 않고 O일 경우... 큐에 담음
        # 방문하지 않았을 경우... 
        # E를 만나면 L을 지났는지 검사
        return [None, None, None]
    
    # s -> l
    # 좌표, L 여부, 이동 횟수
    queue = deque([[s, False, 0]])
    pos, l_visited, cnt = bfs(queue, l, e)
    # print("s->l: ",pos, l_visited, cnt)
    if not l_visited: return -1
    
    # l -> e
    # 좌표, L 여부, 이동 횟수
    queue = deque([[pos, l_visited, cnt]])
    pos, l_visited, cnt = bfs(queue, l, e)
    # print("l->e: ",pos, l_visited, cnt)

    if l_visited:
        return cnt
    else: return -1

# 16
# print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
# # -1
# print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))
# # 7
print(solution(["XXXXX","XXOLO","XOEXO","XOXXO","XSOOO", "XXXXX"]))
# # -1
# print(solution(["XXXXX","XXXLX","XOEXX","XOXXX","XSXXX", "XXXXX"]))
# # -1
# print(solution(["XXXXX","XXXLO","XXEXO","XXXXO","XSOOO", "XXXXX"]))
