'''
민트초코우유: 2025 상반기 오전 1번 (L12)
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/mint-choco-milk/submissions?page=1&page_size=20
소요시간: 4h 15m
[리뷰]
정렬 순서 확실하게 파악하기
중요 조건들, 그때그때 참고하면 좋을 조건들 기록해두기
==이랑 = 구분하기
'''
from pprint import pprint

N, T = map(int, input().split())
F, B = [], []
group = [] # 신봉음식 별 그룹 [F[i][j], g_list]
person = [] # 대표자
visited = [[False]*N for _ in range(N)]
move = [[-1,0], [1,0], [0,-1], [0,1]] # 위, 아래, 왼쪽, 오른쪽
answer_mapping = {'CMT':0, 'CT':1, 'MT':2, 'CM':3, 'M':4, 'C':5, 'T':6}
#### 아침 ####

# 모든 B =+1
def morning():
    global B
    for i in range(N):
        for j in range(N): 
            B[i][j] += 1
    # pprint('morining B')
    # pprint(B)

#### 점심 ####

# 신봉 그룹 나누기 group{M: [[i,j], [i,j],...], T: ...}
def dfs_grouping(g_list, si, sj, f):
    global N, visited, F, B, move
    # 다음 행/열로 ㄱㄱ
    for di, dj in move:
        ni, nj = si+di, sj+dj
        # 갈 수 있음, 방문 안 함, 같은 음식일 경우
        if ni>=0 and nj>=0 and ni<N and nj<N and visited[ni][nj]==False and F[ni][nj]==f:
            # print(ni, nj)
            # print(visited)
            # 방문 체크, 리스트에 추가 [i, j, B]
            visited[ni][nj] = True
            g_list.append([ni, nj, B[ni][nj]])
            # 계속 진행
            dfs_grouping(g_list, ni, nj, f)

def grouping():
    global N, F, group, visited
    # for i in range(N):
    #     for j in range(N):
    #         if not F[i][j] in group:
    #             group[ F[i][j] ] = []
    #         group[ F[i][j] ].append( [i, j, B[i][j]])
    
    # 방문 기록 초기화
    for i in range(N):
        for j in range(N):
            visited[i][j]=False

    # 그룹 초기화
    group = []

    # pprint(F)
    # 맵을 순회하면서
    for i in range(N):
        for j in range(N):
            # 안 간 곳 있으면 리스트 생성 후 dfs
            if not visited[i][j]:
                visited[i][j]=True
                g_list = []
                g_list.append([i, j, B[i][j]])
                # print(i, j, F[i][j])
                dfs_grouping(g_list, i, j, F[i][j])
                group.append([F[i][j], g_list])
    # pprint('group')
    # pprint(group)

# 그룹 내 대표 선출 person [[x, y, 간절함] [] [] []...]
# 대표 신앙심 +() , 나머지 -1
def choose():
    global group, person, B

    # 대표자 초기화
    person = []
    # 그룹 돌아댕기면서
    for _, g_list in group:
        # 각 i j에 대해 B맵의 값이 가장 높은 녀석의 i,j값 반환
        max_person =  max( g_list, key=lambda x:(x[2], -x[0], -x[1]))
        # 대표로 넣기
        person.append( [max_person[0], max_person[1], 0])
        # print(max_person)
        # print(_, g_list)

        # 신앙심 업데이트
        g_len = len(g_list)
        for i, j, _ in g_list:
            if i==max_person[0] and j==max_person[1]:
                B[i][j] += g_len-1
            else:
                B[i][j] -= 1
        # print(B)

    # pprint('B after choose')
    # pprint(B)
    # pprint('person')
    # pprint(person)

### 저녁 ### 

def night():
    global person, visited, F, B, N
    # person 순서 정렬 및 순서대로 진행
    # 음식 수 적음 -> 대표자 신앙심 높음 -> 대표자 행 작음 -> 대표자 열 작음
    person.sort(key=lambda x:(len(F[x[0]][x[1]]), -B[x[0]][x[1]], x[0], x[1]))
    # print('sorted person')
    # print(person)

    # 방문기록 초기화 (용도: 전파를 당했는지!)
    for i in range(N):
        for j in range(N):
            visited[i][j]=False

    for i, j, x in person:

        # 전파 당했으면 전파하지 않음
        if visited[i][j]:
            continue

        # 전파 방향 정함, 간절함, 신앙심 업데이트
        di, dj = move[ B[i][j]%4 ]
        x = B[i][j] - 1
        B[i][j] = 1
        f = F[i][j]
        # 전파 방향대로 계속 이동
        ni, nj = i, j
        while True:
            ni, nj = ni+di, nj+dj
            if ni>=0 and nj>=0 and ni<N and nj<N and x>0:
                # 같은 음식이면 넘어감
                if F[ni][nj]==f:
                    continue
                
                visited[ni][nj] = True
                # print(i, j, '...', ni, nj, visited[ni][nj])
                y = B[ni][nj]
                # 강한 전파
                if x > y:
                    F[ni][nj] = f
                    x -= y+1
                    B[ni][nj] += 1
                # 약한 전파
                else: 
                    F[ni][nj] = ''.join(sorted(set(list(F[ni][nj]) + list(f))))
                    B[ni][nj] += x
                    x = 0
                    break
            else: break
        # print(i, j)
        # print(di, dj)
        # pprint(F)
        # pprint(B)

### 하루 종료 ###

def cal_score():
    global answer_mapping, B, F, N

    score = [0]*7

    # 맵 순회하며 합 누적
    for i in range(N):
        for j in range(N):
            f = F[i][j]
            score[ answer_mapping[f] ] += B[i][j]

    return score

#### MAIN ####

# 초기 입력: 신앙심, 신봉음식 입력받음
for _ in range(N):
    F.append( list(input())  )
for _ in range(N):
    B.append(  list(map(int, input().split()))  )

# pprint('F')
# pprint(F)
# pprint('B')
# pprint(B)

# T일 반복
for _ in range(T):
    # print()

    ### 아침 ###
    # 모든 B =+1
    morning()

    ### 점심 ###

    # 신봉 그룹 나누기 group{M: [[i,j], [i,j],...], T: ...}
    grouping()

    # 그룹 내 대표 선출 person [[x, y, 간절함] [] [] []...]
    # 대표 신앙심 +() , 나머지 -1
    choose()

    ### 저녁 ### 

    # person 순서 정렬 및 순서대로 진행
    # 전파 방향 정함, 간절함, 신앙심 업데이트
    night()

    ### 하루 종료 ###

    # pprint(F)
    # pprint(B)
    # 맵 순회하며 합 누적
    score = cal_score()
    
    # 출력
    print(*score)
