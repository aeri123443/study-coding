'''
미지의 공간 탈출: 2024 하반기 오전 1번 문제 (L14)
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/escape-unknown-space/description
소요시간:6h 29m

[리뷰]
문제 잘못 이해해서 삽질이 심했음 궁금한 점이 생긴다면 기록해두고 바로바로 문제 찾아보기.
애매한 경우는 무조건 문제에서 짚어주니까, 함정이라고 생각하지 말고 그 부분을 좀 찾아보자.
전반적으로 생각하면서 타자 치는 속도가 느린 것 같음. 실수하는 것보단 천천히 하는 게 낫다!지만 이새키는 실수도하고 느리기까지 하네
그래도 이건 반복하다보면 나아질듯
좌표에 변수 안넣고 숫자 넣은거 진짠가 싶다... 2가 아니라 M-1로 했어야지 ㅠㅠ
예약어 함수명에 쓰면 재귀되니까 짧은 단어 쓸 때 조심~!
각 변수 내부에 있는 데이터 형식은 메모장에 적어둬서, 굳이 찾지 않아도 되도록 하자

그래도 포기하지 않고 끝까지 오류 찾아낸거 잘 했어!!
'''
from pprint import pprint

from collections import deque

N, M, F = map(int, input().split())
all_map = { 'floor':[], 'U':[],'E':[], 'W':[], 'S':[], 'N':[] }
extentions = {}      
start = [] # 시작 좌표
to_floor = [] # 바닥으로 갈 수 있는 사이드좌표 정보
q = deque()
visited = { 'floor':[[False]*N for _ in range(N)], 
           'U':[[False]*M for _ in range(M)],
           'E':[[False]*M for _ in range(M)], 
           'W':[[False]*M for _ in range(M)], 
           'S':[[False]*M for _ in range(M)], 
           'N':[[False]*M for _ in range(M)] }

# 시간이상현상 확인법
# : 큐를 확인 후 일정 시간(거리?)지난 상황이면 장애물로 업데이트 (어차피 BFS니까...)

#### 맵 생성 ####
def input_data():
    global N, M, F, all_map

    # 평면맵 (floor)
    tmp = []
    for _ in range(N):
        tmp.append( list(map(int, input().split())) )
    all_map['floor'] = tmp

    # 시간의 벽 맵 ('E', 'W', 'S', 'N', 'U')
    key_list = ['E', 'W', 'S', 'N', 'U']
    for k in key_list:
        tmp = []
        for _ in range(M):
            tmp.append( list(map(int, input().split())) )
        all_map[k] = tmp
     
    # 시간 이상 현상
    for _ in range(F):
        r, c, d, v = map(int, input().split())
        # print(r, c, d, v)
        # 감지T: 이전m, 이전r, 이전c, 감지된m, 감지된r, 감지된c, 속도v, 방향d 
        extentions[v] = [-1, -1, -1, 'floor', r, c, v, d]
        all_map['floor'][r][c] = 1

#### 맵에서 필요한 포인트 찾기 ####
def find_point():
    global M, all_map, start, to_floor

    # 시작 좌표 찾기
    for i in range(M):
        for j in range(M):
            if all_map['U'][i][j]==2:
                start = [i, j]
                break

    # 사이드 - 바닥 유일한 통로 찾기
    # 3(시간의벽) 시작 위치
    s3i, s3j = float('inf'), float('inf')
    for i in range(N):
        flag = False
        for j in range(N):
            # 맵을 탐색하다가 바닥에서 3을 찾으면
            if all_map['floor'][i][j] == 3:
                # 그 상하좌우가 0인 경우를 찾음
                # 3의 오른쪽임 - 동면, 왼쪽임 - 서면, 위쪽임 - 남면, 아래쪽임 - 북면
                # 면 정보와 사이드면의 좌표를 저장

                # 타깃의 상대 위치를 반환
                # 상대위치를 기반으로 사이드면의 통로를 찾음
                s3i, s3j = min(i, s3i), min(j, s3j)
                ti, tj = i-s3i, j-s3j
                # print(s3i, s3j, ti, tj, i, j, i, j-1, all_map['floor'][i][j-1])
                if j+1 < N and all_map['floor'][i][j+1] == 0:
                    to_floor = ['E', M-1, M-ti-1, i, j+1]
                    flag = True
                    break
                elif j-1 >= 0 and all_map['floor'][i][j-1] == 0:
                    to_floor = ['W', M-1, ti, i, j-1]
                    flag = True
                    break
                elif i+1 < N and all_map['floor'][i+1][j] == 0:
                    to_floor = ['S', M-1, tj, i+1, j]
                    flag = True
                    break
                elif i-1 >= 0 and all_map['floor'][i-1][j] == 0:
                    to_floor = ['N', M-1, M-tj-1, i-1, j]
                    flag = True
                    break
        if flag: break

#### 이동 함수 ####
# 진입 좌표 입력 (전 평면)
# 이전-다음 평면에 따라 좌표 계산
# 다음 좌표 반환

# 위에서 사이드로 이동할 때
def up_to_side(i, j, ni, nj):
    global all_map, M
    # print('up_to_side', i, j, ni, nj)
    # j가 커짐: 동쪽 사이드로
    if nj>=M: return ['E', 0, M-i-1]
    # j가 작아짐: 서쪽 사이드로
    elif nj<0: return ['W', 0, i]
    # i가 커짐: 남쪽 사이드로
    elif ni>=M: return ['S', 0, j]
    # i가 작아짐: 북쪽 사이드로
    elif ni<0: return ['N', 0, M-j-1]

# 사이드에서 위로
def side_to_up(m, j):
    global M
    # print('side_to_up', m, j)
    if m == 'E': return [M-j-1, M-1]
    elif m == 'W': return [j, 0]
    elif m == 'S': return [M-1, j]
    elif m == 'N': return [0, M-j-1]

# 사이드에서 사이드로
def side_to_side(m, i, j, nj):
    # print('side_to_side', m, i, j, nj)
    # 이동 방향
    left = {'E':'S', 'S':'W', 'W':'N', 'N':'E'}
    right = {'E':'N', 'N':'W', 'W':'S', 'S':'E'}

    if nj<0:
        return [left[m], i, M-j-1]
    elif nj>=M:
        return [right[m], i, M-j-1]

def return_next(m, i, j, nm, ni, nj):
    global to_floor, all_map

    # 장애물 1은 따로 처리
    # floor: 0보다 작아지거나 N보다 커지면 안됨, 시간의벽3이거나 장애물1이어도 안됨
    #       탈출구4면 탈출
    if m=='floor' and not (ni>=0 and nj>=0 and ni<N and nj<N and all_map['floor'][ni][nj]!=3):
        return [-1, -1, -1]
    # U: 범위 벗어나는 모든 경우에 대해 사이드로 이동, 장애물1은 안됨
    elif m=='U' and not (ni>=0 and nj>=0 and ni<M and nj<M):
        [nm, ni, nj] = up_to_side(i, j, ni, nj)
    # 사이드: 아래로 벗어나면 floor로, 위로 벗어나면 up, 옆으로 벗어나면 다른 사이드로 이동
    elif m=='E' or m=='W' or m=='S' or m=='N':
        if ni>=M: # floor로
            # 아래로 벗어나면... 아래로 갈 수 있는 좌표인지 확인해야함
            [tm, ti, tj, nexti, nextj] = to_floor
            if m==tm and i==ti and j==tj:
                nm, ni, nj = 'floor', nexti, nextj
            else: return [-1, -1, -1]
        elif ni<0: # 위로
            [ni, nj] = side_to_up(m, j)
            nm = 'U'
        elif nj<0 or nj>=M: # 다른 사이드로
            [nm, ni, nj] = side_to_side(m, i, j, nj)

    return [nm, ni, nj]

def bfs():
    global q, start, visited, all_map, to_floor
    
    # 동, 서, 남, 북
    move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    si, sj = start
    # Q [평면정보(m), pm, pi, pj, i, j, t]
    # 디버깅을 위해 이전 좌표도 출력
    q.append([-1, -1, -1, 'U', si, sj, 0])
    visited['U'][si][sj] = True

    while q:
        # Q pop
        pm, pi, pj, m, i, j, t = q.popleft()
        
        # 탈출구 감지
        if all_map[m][i][j] == 4:
            return t
        
        # 이전의 타일이 시간 이상 현상으로 확장되었었으면 넘어감
        if (pm, pi, pj) != (-1,-1,-1) and all_map[pm][pi][pj]==1:
            continue

        # 시간 이상 현상
        tmp_del = []
        tmp_append = []
        for ex in extentions:
            # 시간 이상 현상 발생 시
            if t == ex:
                # 감지T: 이전m, 이전r, 이전c, 감지된m, 감지된r, 감지된c, 속도v, 방향d 
                pem, per, pec, em, er, ec, ev, ed = extentions[ex]
                edr, edc = move[ed]
                nem, ner, nec = em, er+edr, ec+edc

                # 장애물 추가..할건데
                # 다음 좌표가 벽을 넘어갔을 때를 감안해야 함

                # 잘못햇당이런... 필요없엇넹...
                # 1 만나면 바로 사라짐.,
                # 유일통로의 바닥에서 0->3으로 가는 경우이며 통로 이동의 경우 따로 처리가 필요
                if em == 'floor' and er==to_floor[3] and ec==to_floor[4] and ner>=0 and nec>=0 and ner<N and nec<N and all_map['floor'][ner][nec]==3:
                    nem, ner, nec = to_floor[0], to_floor[1], to_floor[2]
                else: 
                    # dl동 불가능한 좌표가 되면 넘어감
                    if not (ner >= 0 and nec >=0 and ner<N and nec<N):
                        continue

                    # [nem, ner, nec] = return_next(em, er, ec, nem, ner, nec)
                
                # 이동불가능한 좌표면 넘어감
                # if (-1,-1,-1) == (nem, ner, nec):
                #     continue

                # 장애물이거나 탈출구일 경우 넘어감
                if all_map[nem][ner][nec] == 1 or all_map[nem][ner][nec] == 4:
                    continue
                
                # 장애물 추가
                all_map[nem][ner][nec] = 1

                # pprint('장애물 추가')
                # pprint(all_map)

                # 방금 사용한 원소는 삭제
                tmp_del.append(ex)
                # 새로운 원소로, 다음 감지 시간을 추가
                tmp_append.append([ex+ev, [em, er, ec, nem, ner, nec, ev, ed]])
                # extentions[ex+ev] = em, er, ec, nem, ner, nec, ev, ed

        for del_key in tmp_del:
            del extentions[del_key]
        for [append_key, append_list] in tmp_append:
            extentions[append_key] = append_list

        # 상하좌우 이동
        for [di, dj] in move:
            nm = m
            ni, nj = i+di, j+dj

            # ni nj가 벽에 막혔을 경우...

            [nm, ni, nj] = return_next(m, i, j, nm, ni, nj)
            # 이동 불가능한 좌표면 패스
            if (nm, ni, nj) == (-1, -1, -1):
                continue
            # floor -> 3으로 갈 때 따로 처리가 필요(막아야 함)
            if nm=='floor' and all_map['floor'][ni][nj]==3:
                continue
        
            # 다음이 장애물이거나, 방문했을 경우 패스
            if all_map[nm][ni][nj]==1 or visited[nm][ni][nj]==True:
                continue
            # print(m, i, j, nm, ni, nj, t+1)
            
            # 모든 조건을 통과했을 경우 큐에 쌓고 방문 체크
            visited[nm][ni][nj]=True
            q.append([m, i, j, nm, ni, nj, t+1])
        # 한번에: ni nj가 미방문 좌표일 경우, 방문처리 후 큐에 쌓기
    # pprint(all_map)
    return -1
#### main ####

input_data()
find_point()
# pprint('input_data')
# pprint(all_map)
# pprint(visited)
# pprint(extentions)
# pprint(start)
# pprint(to_floor)

if to_floor:
    # BFS
    answer = bfs()
    # pprint('after visited')
    # pprint(visited)

    print(answer)
else:
    print(-1)
