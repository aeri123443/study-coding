'''
p.180 14. 표 편집
https://school.programmers.co.kr/learn/courses/30/lessons/81303
소요시간: 97m 14s
'''

visited = []
n = 0 # 던전 수
answer = 0

def dfs(dungeons, hp, max_num):
    global visited, n, answer

    # 최대값이면 통과
    if max_num == n:
        answer = n
        return True
    
    # 최대값 갱신
    answer = max(answer, max_num)

    for i in range(n):
        # 방문하지 않았고, 진입 가능한지
        if (not visited[i]) and (hp >= dungeons[i][0]):
            visited[i] = True
            dfs(dungeons, hp-dungeons[i][1], max_num+1)
            visited[i] = False
                
def solution(k, dungeons):
    global answer, visited, n

    n = len(dungeons)
    visited = [False]*n

    dfs(dungeons, k, 0)
    return answer


# 3
print(solution(80, [[80, 20], [50, 40], [30, 10]]))
      