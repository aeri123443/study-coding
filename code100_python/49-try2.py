'''
p.497 49. 피로도
https://school.programmers.co.kr/learn/courses/30/lessons/87946
visited 활용, 깔끔하게 풀어보기
'''

def dfs(dungeons, hp, num):
    global N, answer

    if num == N:
        answer = num
        return
    
    answer = max(answer, num)
    for i, [need, damage] in enumerate(dungeons):
        if not visited[i] and hp>=need:
            remain_hp = hp - damage
            visited[i] = True
            dfs(dungeons, remain_hp, num+1)
            visited[i] = False

def solution(k, dungeons):
    global answer, visited, N
    N = len(dungeons)
    answer = 0
    visited = [False]*N
    
    dfs(dungeons, k, 0)

    return answer


print(solution(80, [[80,20],[50,40],[30,10]]))
print(solution(100, [[100, 20], [60, 30], [50, 20], [10, 20]]))
print(solution(100, [[100, 20], [60, 30], [50, 20], [40, 20]]))
