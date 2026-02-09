
'''
Lv. 2 [PCCP 모의고사 #1] 2번 - 체육대회
https://school.programmers.co.kr/learn/courses/20847/lessons/255901
11m 40s
'''

'''
체육대회는 여러 종목에 대해 각 반의 해당 종목 대표가 1명씩 나와 대결을 하며
한 학생은 최대 한개의 종목 대표만
각 종목 대표의 해당 종목에 대한 능력치의 합을 최대화하는 것
'''

def solution(ability):
    mem_num = len(ability)
    sports_num = len(ability[0])

    answer = 0
    visited = [False]*mem_num
    def dfs(n, total):
        nonlocal answer

        if n==sports_num:
            answer = max(answer, total)
            return
        
        for i in range(mem_num):
            if not visited[i]:
                visited[i] = True
                dfs(n+1, total+ability[i][n])
                visited[i] = False

    dfs(0, 0)            
    return answer

print()
print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))
print(210)

print()
print(solution([[20, 30], [30, 20], [20, 30]]))
print(60)

# print()
# print(solution())
# print()