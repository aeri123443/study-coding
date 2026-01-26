'''
1149. <실버 1> RGB거리
https://www.acmicpc.net/problem/1149
백트래킹은 시간초과
'''

import sys
input = sys.stdin.readline

N = int(input())
houses = []
# R:0, G:1, B:2
for _ in range(N):
    houses.append( list(map(int, input().split())) )
# print(houses)

min_cost = float('inf')
def coloring(cnt, cost, rgb):
    global min_cost
    # print('coloring...cnt, cost, rgb:', cnt, cost, rgb)

    if min_cost < cost:
        return
    # if cnt==N:
    #     min_cost = min(min_cost, cost)
    #     return

    for i in range(3):
        # print(cnt, i)
        if i != rgb:
            if cnt==N-1:
                min_cost = min(min_cost, cost+houses[cnt][i])
            else:
                coloring(cnt+1, cost+houses[cnt][i], i)

coloring(0, 0, -1)  
print(min_cost)  
