'''
1018. 체스판 다시 칠하기
https://www.acmicpc.net/problem/1018
'''
N, M = map(int, input().split())
input_list = [list(input()) for _ in range(N)]

# 영역 잡고
start_list = []
for i in range(N-7):
    for j in range(M-7):
        start_list.append([i,j])

# T/F로 매핑
for i in range(N):
    for j in range(M):
        if input_list[i][j]=='B':
            input_list[i][j]=True
        else: input_list[i][j]=False

# 계산해보고
def sol(start, input_list, x, y):
    global answer
    cnt = 0
    up = start
    left = start
    for i in range(x, x+8):
        for j in range(y, y+8):
            if j==y:
                if up == input_list[i][j]:
                    # print(i, j, 'replace down', input_list[i][j], '->', not input_list[i][j])
                    cnt += 1
                    if answer <= cnt:
                        return answer
                up = not up
                left = up
            else:
                if left == input_list[i][j]:
                    # print(i, j, 'replace right', input_list[i][j], '->', not input_list[i][j])
                    cnt +=1
                    if answer <= cnt:
                        return answer
                left = not left
    return cnt
    
answer = float('inf')
for x,y in start_list:
    for start in [True, False]:
        cnt = sol(start, input_list, x, y)
        answer = min(answer, cnt)

print(answer)
