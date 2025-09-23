'''
2025 상반기 오후 1번 문제
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/microbial-research/description
갈아엎기 전 포함해서 12~13시간 만에 풀었다 와우
'''
from pprint import pprint

### 1단계: 미생물 투입 ###

# 투입하면서 겹치는 영역 교체 / 교체된 무리 기록
def insert(i):
    global arr1
    replaced = set()

    # 값 입력 받고
    r1, c1, r2, c2 = map(int, input().split())
    # print(r1, c1, r2, c2)
    # 입력받은 값에 대해 하나씩 대입
    for r in range(r1, r2):
        for c in range(c1, c2):
            # 겹치는 놈이 있으면 그 놈을 replaced에 넣고 덮어쓰기
            if arr1[c][r] != -1:
                replaced.add(arr1[c][r])
            arr1[c][r] = i
    # pprint(arr1)
    # print(replaced)
    return replaced

# dfs로 연결된 셀 방문처리
def dfs_group(i, sr, sc):
    global arr1, visited, N
    # move 선언
    move = [[1, 0], [-1, 0], [0,1], [0,-1]]
    # 다음이 이동 가능한 좌표일 경우 (i이고, 최대최소 안 넘기고) 재귀 선언
    for dc, dr in move:
        nc, nr = sc+dc, sr+dr
        if nc>=0 and nr>=0 and nc<N and nr<N and arr1[nc][nr]==i and visited[nc][nr]==False:
            visited[nc][nr]=True
            dfs_group(i, nr, nc)

# 교체된 무리의 영역 분리 확인(완전 탐색) 후 분리된 미생물 무리 삭제 
def group():
    global arr1, N, visited, areas

    # 무리 당 그룹 수
    group_count = {}
    # 방문 여부 초기화
    for i in range(N):
        for j in range(N):
            visited[i][j] = False

    # 모든 셀 탐색 후 그룹 확인
    for r in range(N):
        for c in range(N):
            if visited[c][r]==False and arr1[c][r]!=-1:
                # 무리의 그룹 수 업데이트
                if arr1[c][r] not in group_count:
                    group_count[ arr1[c][r] ] = 1
                else:
                    group_count[ arr1[c][r] ] += 1
                # dfs로 연결된 셀 방문처리
                dfs_group(arr1[c][r], r, c)
    # pprint(visited)
    # pprint(group_count)

    # 분리된 미생물 무리 삭제 
    del_key = []
    for gc in group_count:
        if group_count[gc] > 1:
            del_key.append(gc)
    for dk in del_key:
        del group_count[dk]
    # pprint(group_count)
    
    # 남은 무리를 areas에 담음 areas[i] = [i무리의 넓이, [상대 위치들..]]
    areas = {i:[0, []] for i in group_count.keys()}
    min_rc = {i:[float('inf'), float('inf')] for i in group_count.keys()}
    for c in range(N):
        for r in range(N):
            i = arr1[c][r]
            if i in areas:
                areas[i][0] += 1
                areas[i][1].append([r, c])
                min_rc[i][0] = min(min_rc[i][0], r)
                min_rc[i][1] = min(min_rc[i][1], c)

    # 각 무리의 좌표를 0,0기준 좌표로 반환
    for i, [_, lst] in areas.items():
       for k in range(len(lst)):
           lst[k] = [lst[k][0]-min_rc[i][0], lst[k][1]-min_rc[i][1]]
    # pprint(areas)    

### 2단계: 배양 용기 이동 ###

# 배치 가능 최소 좌표 찾기
def check(i):
    global areas, N

    # 전체 좌표를 순회하면서
    for sr in range(N):
        for sc in range(N):
            # 대입할 수 있으면 반환
            # 벽을 안 넘고, 아래 뭐가 없고...
            flag = True
            for dr, dc in areas[i][1]:
                nr, nc = sr+dr, sc+dc
                if not (nr<N and nc<N and arr2[nc][nr]==-1):
                    flag = False
                    break
            if flag: return sr, sc
    return -1, -1
                                
def move():
    global areas, N, arr2

    # 미생물무리 넓이 순 정렬
    sorted_areas = [ [k, v[0]] for k, v in areas.items()]
    sorted_areas.sort(key=lambda x:(-x[1], x[0]))
    # pprint('sorted_areas')
    # print(sorted_areas)

    # 배치 가능 좌표 확인 후 대입
    # 배치 불가하면 areas에서 삭제
    for i, w in sorted_areas:
        sr, sc = check(i)
        if (sr, sc) == (-1, -1):
            continue
        # print(i, sr, sc)
        for dr, dc in areas[i][1]:
            nr, nc = sr+dr, sc+dc
            arr2[nc][nr] = i
    # print('arr2')
    # pprint(arr2)

### 3단계: 점수 계산 ###

def check_neighbor():
    global N, neighbor, areas, arr2
    neighbor = { i:set() for i in areas} # 오름차순 기록
    move = [[1,0], [0,1]]

    # 인접 셀 확인
    # 계산되지 않은 인접셀이면, 인접 관계 기록 [a, b] 오름차순
    for c in range(N):
        for r in range(N):
            i = arr2[c][r]
            if i==-1: continue
            for dc, dr in move:
                nc, nr = c+dc, r+dr
                if nc>=N or nr>=N: 
                    continue
                ni = arr2[nc][nr]
                if i!=ni and ni!=-1:
                    if i<ni: neighbor[i].add(ni)
                    else: neighbor[ni].add(i)
    # print('neighbor', neighbor)

def score():
    global neighbor, areas
    # 인접 셀 확인
    # 계산되지 않은 인접셀이면, 인접 관계 기록(오름차순))
    check_neighbor()

    # 최종 점수 계산 및 반환 (미생물, 너비 정보 필요 areas)
    answer = 0
    for i, n_set in neighbor.items():
        for n in n_set:
            answer += areas[i][0]*areas[n][0]
    # print('answer', answer)

    return answer

#### main ####
N, Q = map(int, input().split())
arr1 = [[-1]*N for _ in range(N)] # 단계1 결과맵
arr2 = [[-1]*N for _ in range(N)] # 단계2 결과맵
areas = {}
visited = [[False]*N for _ in range(N)]
neighbor = []

for i in range(Q):
    # print()
    ### 1단계: 미생물 투입 ###
    # 투입하면서 겹치는 영역 교체 / 교체된 무리 기록
    replaced = insert(i)
    # 교체된 무리의 영역 분리 확인(완전 탐색) 후 분리된 미생물 무리 삭제 
    # 남은 무리를 areas에 담음 areas[i] = [i무리의 넓이, [상대 위치들..]]
    group_keys = group()
    # pprint('arr1')
    # pprint(arr1)
    # pprint(areas)

    ### 2단계: 배양 용기 이동 ###
    # 미생물무리 넓이 순 정렬
    # 배치 가능 좌표 확인 후 대입
    # 배치 불가하면 areas에서 삭제
    move()
    # pprint('arr2')
    # pprint(arr2)
    # pprint('areas')
    # pprint(areas, depth=2)

    ### 3단계: 점수 계산 ###
    # 인접 셀 확인
    # 계산되지 않은 인접셀이면, 인접 관계 기록 [a, b] 
    answer = score()
    # 최종 점수 계산 및 반환 (미생물, 너비 정보 필요 areas)
    print(answer)

    ### 4단계: 단계맵 초기화 ###
    for i in range(N):
        for j in range(N):
            arr1[i][j] = arr2[i][j]
    arr2 = [[-1]*N for _ in range(N)]
