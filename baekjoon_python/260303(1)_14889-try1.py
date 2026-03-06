'''
14889. <> 스타트와 링크
https://www.acmicpc.net/problem/14889


'''
import sys
input = sys.stdin.readline
# from pprint import pprint

# N 집, M 치킨집
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

# 일반집, 치킨집 정보 업데이트
# 0은 빈 칸, 1은 집, 2는 치킨집
houses = []
chickens = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1: houses.append( (i,j) )
        elif city[i][j] == 2: chickens.append( (i,j) )

print('houses 1', houses)
print('chickens 2', chickens)

# 치킨집 - 가정집 거리 배열
# (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|
distance = []
for ci, cj in chickens:

    tmp_arr = []
    for hi, hj in houses:
        tmp_arr.append(abs(hi-ci) + abs(hj-cj))
    distance.append(tmp_arr)

for x in distance: print(x)

# del 치킨집 탐색 
# 지워도 min값이 가장 작은 쪽(최대한 유지되는 쪽)을 선택
min_del = [M+1,float('inf')] # (idx, 거리)

del_idx = 0
tmp_min = []

# 가정집 하나 당, 어떤 치킨집이 가까운지 확인
# 이때 (예비)삭제로 선택한 치킨집은 제외
for j in range(N):

    # 이 집에서 가장 가까운 치킨집은?
    near_chiken = [-1, float('inf')]
    for i in range(M):
        if i==del_idx: continue

        if distance[i][j] < near_chiken[1]:

    # if i==del_idx: continue

