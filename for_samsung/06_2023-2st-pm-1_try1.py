'''
루돌프의 반란: 2023 하반기 오후 1번 문제 (L14)
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/rudolph-rebellion/description
소요시간: " 갈 아 엎 음 "

[리뷰]

'''

from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')

N, M, P, C, D = map(int, input().split())
T = 0 # 턴 전역변수로
board = [[0]*N for _ in range(N)]
scores = { i+1:0 for i in range(P) } # 산타 점수
conditions = {i+1:True for i in range(P)} # 기절 False, 탈락시 제거
wake_up = {} # 기절한 산타가 있을 경우, 깨워야 할 때 사용
pos = {} # 각 말의 위치 저장 (현재 위치, 이동 방향)
move4 = [[-1, 0], [0, 1], [1, 0], [0, -1]]
move8 = [[-1, 0], [-1,1], [0, 1], [1,1], [1, 0], [1,-1], [0, -1], [-1,-1]]
#### 데이터 입력 및 초기화 ####

### 데이터 입력
def input_data():
    global N, P, board, scores, pos

    ## 루돌프 위치
    r, c = map(int, input().split())
    # 맵과 위치에 기록
    board[r-1][c-1] = 'X'
    pos['X'] = [r-1, c-1, []]
    # 각 산타 위치
    for _ in range(P):
        # 맵과 위치, 점수, 상태 기록
        i, r, c = map(int, input().split())
        board[r-1][c-1] = i
        pos[i] = [r-1, c-1, []]

#### 캐릭터 이동 ####

### 거리 계산
def cal_dis():
    global board, pos

    # 루돌프 위치 반환
    rx, cx, _ = pos['X']

    # 가장 가까운 산타!!
    # [산타번호, 거리, r, c]
    near_santa = [0, float('inf'), -1, -1]
    # 디버깅 용: 산타 거리 리스트 저장 (추후 주석처리)
    santas_dis = []

    # 각 산타에 대해
    for i in conditions:
        # 산타 위치 반환
        r, c, _ = pos[i]
        # 산타 번호, 거리 저장
        tmp_santa = [i, (r-rx)**2+(c-cx)**2, r, c]
        santas_dis.append(tmp_santa)

        # 산타 업데이트
        near_santa = min(tmp_santa, near_santa, key=lambda x:(x[1], -x[2], -x[3]))

    pprint(santas_dis)
    return near_santa

###  이동 방향 결정
def choose_direction(a, b):
    global board, pos, move4, N
    dis_list = []
    # print(pos[a])
    # print(pos[b])
    ar, ac, _ = pos[a]
    br, bc, _ = pos[b]

    if a == 'X':  # 루돌프가 이동할 경우
        dc, dr = 0, 0
        if ac > bc: dc = -1
        elif ac < bc: dc = 1

        if ar > br: dr = -1
        elif ar < br: dr = 1

        # r, c값이 같으면 이동 방향이 정해짐
        if ac==bc: return [_, dr+ar, ac, dr, 0]
        if ar==br: return [_, ar, dc+ac, 0, dc]
        ## 이동 후 거리 계산

        # print(dc, dr)
        for ddr, ddc in [[dr, 0], [0, dc], [dr, dc]]:
            # print(ddr, ddc)
            nr, nc = ddr+ar, ddc+ac
            dis_list.append([(nr-br)**2+(nc-bc)**2, nr, nc, ddr, ddc])

        pprint(dis_list)
        return min(dis_list, key=lambda x: x[0])

    else: # 산타가 이동할 경우
        for idx, [dr, dc] in enumerate(move4):
            nr, nc = dr + ar, dc + ac
            # 이동 불가능한 좌표면 안 됨
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            # 해당 좌표에 루돌프가 있거나, 빈 곳이여야 함 (다른 산타 있으면 안됨)
            if board[nr][nc] == 'X' or board[nr][nc] == 0:
                dis_list.append([(nr - br) ** 2 + (nc - bc) ** 2, nr, nc, idx])

        pprint(dis_list)
        return min(dis_list, key=lambda x: (x[0], x[3]))

### 이동시키기
def move_character(target, nr, nc):
    global board, pos

    r, c, _ = pos[target]
    board[r][c] = 0
    board[nr][nc] = target
    pos[target] = [nr, nc, []]
#### 충돌 및 상호작용 ####

### 충돌
def meet(a, b, r, c, dr, dc): # a:이동한 애 b: 부딪힌 애
    global board, pos, scores, conditions, wake_up, N, C, D, T
    ar, ac, _ = pos[a]
    br, bc, _ = pos[b]

    if a == 'X': # 루돌프가 이동했을 경우
        scores[b] += C
        nr, nc = br+(dr*C), bc+(dc*C)

        # 게임 밖으로 이동한 산타는 탈락 / 탈락하지 않았다면 기절시킴
        if not (0 <= nr < N and 0 <= nc < N):
            print("산타", b, "탈락")
            del conditions[b]
            board[br][bc] = 0
            move_character(a, r, c)
            return
        else:
            print("산타", b, "기절1")
            conditions[b] = False
            # 2턴 후 활동 가능
            if T+2 in wake_up:
                wake_up[T+2].append(b)
            else:
                wake_up[T+2] = [b]

        # 이동 위치에 다른 산타가 있었을 경우 재귀 실행
        if board[nr][nc] != 0:
            meet(b, board[nr][nc], nr, nc, dr, dc)

        move_character(b, nr, nc)
        move_character(a, r, c)

    elif b == 'X': # 루돌프가 충돌당함 (=산타가 이동함)
        scores[a] += D
        print(ar, ac)
        nr, nc = r-(dr*D), c-(dc*D)

        # 게임 밖으로 이동한 산타는 탈락
        if not (0 <= nr < N and 0 <= nc < N):
            print("산타", a, "탈락")
            del conditions[a]
            board[ar][ac] = 0
            return
        else:
            print("산타", a, "기절2")
            print(nr,nc)
            conditions[a] = False
            # 2턴 후 활동 가능
            if T+2 in wake_up:
                wake_up[T+2].append(a)
            else:
                wake_up[T+2] = [a]

        # 이동 위치에 다른 산타가 있었을 경우 재귀 실행
        if board[nr][nc] != 0:
            meet(a, board[nr][nc], nr, nc, -dr, -dc)

        print('move_character1(a, r, c)', a, nr, nc)
        move_character(a, nr, nc)
        pprint(board)

    else: # 산타와 산타 충돌 (상호작용)
        print("산타", a, b, "충돌")

        # b의 이동 방향
        print(r, c)
        nr, nc = r + dr, c + dc

        # 게임 밖으로 이동한 산타는 탈락
        if not (0 <= nr < N and 0 <= nc < N):
            print("산타", b, "탈락")
            del conditions[b]
            board[br][bc] = 0
            return
        else:
            pprint(board)
            print('move_character2(b, nr, nc)', b, nr, nc)
            move_character(b, nr, nc)
            pprint(board)

        # 이동 위치에 다른 산타가 있었을 경우 재귀 실행
        if board[nr][nc] != 0:
            if board[nr][nc] != b:
                meet(b, board[nr][nc], nr, nc, dr, dc)

        print('move_character3(a, r, c)', a, r, c)
        move_character(a, r, c)
        pprint(board)


#### main ####

### 데이터 입력
input_data()

pprint(pos)
pprint(board)

for _ in range(M):
    print('')
    print(T)

    ### 기절한 산타 깨우기
    if T in wake_up:
        for sleeping_santa in wake_up[T]:
            if sleeping_santa in conditions:
                print(sleeping_santa, 'wake_up')
                conditions[sleeping_santa] = True
        del wake_up[T]

    ### 루돌프 이동

    ## 거리 계산
    near_santa_num, near_santa_dis, near_santa_r, near_santa_c = cal_dis()
    pprint('가까운 산타')
    print(near_santa_num, near_santa_dis, near_santa_r, near_santa_c)

    ## 이동 방향 결정
    chose_dis, chose_nr, chose_nc, chose_ddr, chose_ddc = choose_direction('X', near_santa_num)
    pprint('이동 방향 결정')
    print(chose_dis, chose_nr, chose_nc, chose_ddr, chose_ddc)

    ## 이동하려는 위치에 산타가 있는지
    if board[chose_nr][chose_nc] != 0:
        meet('X', board[chose_nr][chose_nc], chose_nr, chose_nc, chose_ddr, chose_ddc)
    else:
        move_character('X', chose_nr, chose_nc)

    pprint('루돌프 이동 결과')
    pprint(board)

    ### 산타 이동
    for i in range(P):
        santa_name = i+1
        print(santa_name)

        # 기절했거나 탈락한 산타는 넘어감
        if (not santa_name in conditions) or (not conditions[santa_name]):
            continue

        # 산타->루돌프 가까운 방향 확인
        chose_dis, chose_nr, chose_nc, chose_move_idx = choose_direction(santa_name, 'X')
        print(chose_dis, chose_nr, chose_nc, chose_move_idx)

        ## 이동하려는 위치에 루돌프가 있는지
        if board[chose_nr][chose_nc] == 'X':
            meet(santa_name, 'X', chose_nr, chose_nc, *move4[chose_move_idx])
        else:
            move_character(santa_name, chose_nr, chose_nc)
        pprint('산타 이동 결과')
        pprint(board)

    ### 살아남은 산타 점수 추가
    for santa_name in conditions:
        scores[santa_name] += 1

    pprint('scores')
    pprint(scores)

    T += 1

    ### 종료 조건
    # 남은 산타가 없으면 종료
    if len(conditions) == 0: break

