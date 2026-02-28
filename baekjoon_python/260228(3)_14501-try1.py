'''
14501. <실버 3> 퇴사
https://www.acmicpc.net/problem/14501

Total 17m 1s
문제 분석 8m 6s
코드 작성 8m 55s
오류 수정 0m 0s

dp로도 풀 수 있었음!
'''
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)

answer = 0
def dfs(idx, pay): 
    global answer

    if idx >= N:
        answer = max(answer, pay)
        return
    t, p = arr[idx]

    # idx 상담 잡음
    if idx+t <= N:
        dfs(idx+t, pay+p)
    
    # idx 상담 잡지 않음
    dfs(idx+1, pay)

dfs(0, 0)
print(answer)