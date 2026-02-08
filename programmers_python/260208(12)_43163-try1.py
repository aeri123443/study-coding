'''
43163. lv3 단어 변환
https://school.programmers.co.kr/learn/courses/30/lessons/43163
29m 47s
'''

import sys
sys.setrecursionlimit(int(1e6))

# 다음 단계로 진행할 수 있는지 확인
# 하나의 단어만 차이가 나야 함
def is_possible(n, s1, s2):
    diff = 0
    for i in range(n):
        if s1[i] != s2[i]:
            if diff==0:
                diff+=1
            else: # 1개 이상 다르단 뜻!
                return False
            
    return True if diff == 1 else False

def solution(begin, target, words):
    INF = float('inf')
    n = len(words[0])
    answer = INF
    visited = [False]*len(words)

    if target not in words:
        return 0

    def backtracking(s, cnt):
        nonlocal answer

        # print(s, cnt)

        if s == target:
            answer = min(cnt, answer)
            return
        
        if cnt >= answer:
            return
        
        for i, x in enumerate(words):
            if not visited[i] and is_possible(n, s, x):
                visited[i] = True
                backtracking(x, cnt+1)
                visited[i] = False

    backtracking(begin, 0)    

    return answer if answer != INF else 0

print()
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(4)

print()
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
print(0)

# print()
# print(solution())
# print()