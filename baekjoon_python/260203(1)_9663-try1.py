'''
9663. <골드 4> N-Queen
https://www.acmicpc.net/problem/9663
'''

N = int(input())

col = [False]*N
pos = [False]*(2*N-1) # 우측 상향 대각선
neg = [False]*(2*N-1) # 좌측 하향 대각선

cnt = 0

def dfs(i):
    global cnt
    # print(i)
    for j in range(N):
        # print(i,'````')
        # 방문을 하나라도 했으면 패스
        # print(i, j, i+j, i-j+N-1)
        if col[j] or pos[i+j] or neg[i-j+N-1]:
            continue
        if i == N-1:
            # print(i, j)
            cnt+=1
            continue
        # print('ok')
        col[j] = pos[i+j] = neg[i-j+N-1] = True
        dfs(i+1)
        col[j] = pos[i+j] = neg[i-j+N-1] = False

dfs(0)
print(cnt)