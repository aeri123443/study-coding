'''
87946. lv2 피로도
https://school.programmers.co.kr/learn/courses/30/lessons/87946
17m 0s
'''

def solution(k, dungeons):
    N = len(dungeons)

    answer = 0
    visited = [False]*N

    def backtracking(cur_hp, cur_cnt):
        nonlocal answer

        if cur_cnt == N:
            answer = N
            return
        
        answer = max(answer, cur_cnt)

        for i in range(N):
            if not visited[i] and cur_hp >= dungeons[i][0]:
                visited[i] = True
                backtracking(cur_hp-dungeons[i][1], cur_cnt+1)
                visited[i] = False

    backtracking(k, 0)

    return answer

print()
print(solution(80, [[80,20],[50,40],[30,10]]))
print(3)
