'''
2025 상반기 오후 1번 문제
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/microbial-research/description
문제 제대로 분석하고 다시 풀기
'''
from pprint import pprint

import heapq

def step1(i):
    print('step1')
    global arr1, areas, N
    r1, c1, r2, c2 = map(int, input().split())
    print(arr1)

    # 넓이(정수), 모양(2차원 배열)
    areas[i] = [(r2-r1)*(c2-c1), [[1]*(r2-r1) for _ in range(c2-c1)]]

    # 배치하면서 숫자가 겹치는 칸 기록
    replaced = set()
    for r in range(r1, r2):
        for c in range(c1, c2):
            if arr1[c][r] != -1:
                [pi, pr, pc] = arr1[c][r]
                areas[pi][0] -= 1
                areas[pi][1][pc][pr] = 0
                # heapq.heappush(areas, [-1*(r2-r1)*(c2-c1), i])
                replaced.add(arr1[c][r][0])
            arr1[c][r] = [i, r-r1, c-c1] # 상대위치도 함께 저장

    pprint(areas)
    print(replaced)
    pprint(arr1)
    print()

#### step 2 ####

# 시작 좌표 반환하기
def check(i):
    print('check', i)

    global N, areas, arr2
    # 전체 평면을 돌면서
    for sr in range(N):
        for sc in range(N):
            # 상대좌표에 대해 모두 대입 가능하면 통과
            # 1. 최대 높이/너비 이하인지
            # 2. 이미 arr2에 값이 존재하는지
            for r in range(len(areas[i][1][0])):
                for c in range(len(areas[i][1])):
                    if areas[i][1][c][r] == 1:
                        nr, nc = sr+r, sc+c
                        if nr < N and nc < N and arr2[nc][nr]==-1:
                            return sr, sc
    return -1, -1

def step2():
    print('step2')

    global N, areas, arr1, arr2
    sorted_list = sorted(areas.items(), key=lambda x:x[1][0], reverse=True)
    print(sorted_list)
    for i, [a, s_list] in sorted_list:
        print(check(i))
        # 시작 좌표 찾고
        # 상대위치 참고해서 arr2에 대입
        sr, sc = check(i)
        for r in range(len(areas[i][1][0])):
            for c in range(len(areas[i][1])):
                if areas[i][1][c][r] == 1:
                    nr, nc = sr+r, sc+c
                    arr2[nc][nr]=i
        pprint(arr2)

    # 최대한 높은 y축, 

#### main ####
N, Q = map(int, input().split())
arr1 = [[-1]*N for _ in range(N)] # 단계1 결과맵
arr2 = [[-1]*N for _ in range(N)] # 단계2 결과맵
areas = {}
for i in range(Q):
    # 1단계
    step1(i)
    print()
    step2()
    print()

    # 결과맵 초기화
    for i in range(N):
        for j in range(N):
            arr1[i][j] = arr2[i][j]
    arr2 = [[-1]*N for _ in range(N)]
