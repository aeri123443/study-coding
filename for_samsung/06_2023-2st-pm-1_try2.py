'''
루돌프의 반란: 2023 하반기 오후 1번 문제 (L14)
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/rudolph-rebellion/description
소요시간: 3h 28m

[리뷰]

'''
from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')

#### 보조 함수 ####

### 거리 계산
def cal_distance(r1, c1, r2, c2):
    return (r1 - r2)**2 + (c1 - c2)**2

### 생존 산타 확인
def is_santa_there():
    global board, santas
    for s in santas:
        # 탈락하지 않은 산타가 하나라도 있으면 True
        if not s.is_out:
            return True

    return False

### 디버깅: 턴 결과 확인
def turn_result():
    global board, santas, T

    print()
    print('turn', T, 'end...')
    pprint(board)
    print('santas: s.name, s.score, s.is_out, s.is_sleep, s.pos')
    for s in santas:
        print(s.name, s.score, s.is_out, s.is_sleep, s.pos)

#### 산타 클래스 ###
class Santa:
    def __init__(self, _name=1, _r=0, _c=0):
        self.name = _name
        self.pos = (_r, _c)
        self.score = 0
        self.is_sleep = False
        self.is_out = False

    # 루돌프와 가까운 방향 찾기
    def check_direction(self, ru):
        move = [[-1,0], [0,1], [1,0], [0,-1]]

        # 초기 거리 (가까워지는 기준)
        defalut_distance = cal_distance(self.pos[0], self.pos[1], ru.pos[0], ru.pos[1])

        # 4회 반복
        tmp_list = []
        for i in range(4):
            dr, dc = move[i]
            nr, nc = self.pos[0]+dr, self.pos[1]+dc

            # 다른 산타가 있어도 안됨!!
            if not (0<=nr<N and 0<=nc<N and board[nr][nc]<=0):
                continue

            # 각 이동에 대한 거리 계산
            tmp_distance = cal_distance(nr, nc, *ru.pos)
            # 현 거리에 비해 가까워지는지 확인
            if tmp_distance < defalut_distance:
                tmp_list.append([tmp_distance, i])

        # 가까운 방향 반환
        # pprint('현 거리')
        # pprint(defalut_distance)
        # pprint('산타->루돌프 temp_list: dis, move_idx')
        # pprint(tmp_list)

        # 움직이지 않을 경우 -1, -1 반환
        if not tmp_list:
            return [-1, -1]

        # 가장 가까운 애 (조건 포함)
        near_dir = min(tmp_list, key=lambda x:(x[0], x[1]))
        # print('산타->루돌프 near_dir: ', near_dir)

        return move[ near_dir[1] ] # [dr, dc]

    def move(self, dr, dc):
        global board, santas, D, T
        nr, nc = self.pos[0] + dr, self.pos[1] + dc

        # 범위 밖을 넘어가면 탈락
        if not (0<=nr<N and 0<=nc<N):
            # print('산타', self.name, '탈락')
            self.is_out = True
            board[ self.pos[0] ][ self.pos[1] ] = 0
            self.pos = (-1, -1)
            return [-1, -1]

        # 그 자리에 다른 산타/루돌프가 있을 경우 산타부터 이동시킴
        if board[nr][nc] == -1: # 루돌프가 있었다! (충돌)
            self.score += D
            # print('-dr*D, -dc*D',-dr*D, -dc*D)
            # 한 방향으로 갔다가 반대 방향으로 간 거니까, 그 과정을 반영해야 함
            move_result = self.move(dr-dr*D, dc-dc*D)

            # 산타 이동 결과가 탈락일 경우 패스
            if move_result == [-1, -1]:
                return [-1, -1]

            # 탈락이 아니면 산타 기절
            # print("산타", self.name, "기절")
            self.is_sleep = T+2
            return # 이동을 완료했으므로 이후의 코드를 실행하지 않음

        elif board[nr][nc] > 0: # 다른 산타가 있었다! (상호작용)
            # 자기 자신이면 넘어감
            if board[nr][nc] != self.name:
                # 그 산타를 한 칸 더 이동시킴
                target_san = santas[board[nr][nc]-1]
                # print('target_san', target_san.name)
                if dr>0: new_dr = 1
                elif dr<0: new_dr = -1
                else: new_dr = 0
                if dc>0: new_dc = 1
                elif dc<0: new_dc = -1
                else: new_dc = 0

                target_san.move(new_dr, new_dc)

        board[self.pos[0]][self.pos[1]] = 0
        board[nr][nc] = self.name
        self.pos = (nr, nc)

#### 루돌프 클래스 ####
class Rudolf:
    def __init__(self, _r=0, _c=0):
        self.pos = (_r, _c)

    # 산타와 가까운 거리 찾기
    def check_near_santa(self):
        global santas, P

        tmp_list = []
        # 산타 반복문
        for s in santas:
            # 탈락한 산타 제외
            if s.is_out: continue
            tmp_list.append([ cal_distance(*ru.pos, *s.pos), *s.pos, s ])

        # pprint('temp_list: dis, san_r, san_c, san_class')
        # print(tmp_list)
        # 가장 가까운 애 (조건 포함)
        near_santa = min(tmp_list, key=lambda x:(x[0], -x[1], -x[2]))
        # print('near_santa: ', near_santa[3].name, near_santa)

        return near_santa[3]

    # 산타에게 갈 가장 가까운 방향 찾기
    def check_direction(self, san):
        move = [[-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1]]

        # 8회 반복
        tmp_list = []
        for dr, dc in move:
            nr, nc = self.pos[0]+dr, self.pos[1]+dc
            if not (0<=nr<N and 0<=nc<N):
                continue
            # 각 이동에 대한 거리 계산
            tmp_list.append([cal_distance(nr, nc, *san.pos), dr, dc])

        # 가까운 방향 반환
        # pprint('temp_list: dis, dr, dc')
        # pprint(tmp_list)
        # 가장 가까운 애 (조건 포함)
        near_dir = min(tmp_list, key=lambda x:x[0])
        # print('near_dir: ', near_dir)
        return [near_dir[1], near_dir[2]]

    def move(self, dr, dc):
        global board, C, T
        nr, nc = self.pos[0]+dr, self.pos[1]+dc

        # 그 자리에 산타가 있을 경우 산타부터 이동시킴
        if board[nr][nc] > 0:
            target_san = santas[board[nr][nc] - 1]
            # print('target_san', target_san.name)
            target_san.score += C
            target_san.move(dr*C, dc*C)
            # 해당 산타 기절시킴
            # print('산타', target_san.name, '기절')
            target_san.is_sleep = T+2

        board[self.pos[0]][self.pos[1]] = 0
        board[nr][nc] = -1
        self.pos = (nr, nc)

#### 데이터 입력 ####

def input_data():
    global P, ru, santas, board

    # 루돌프
    r, c = map(int, input().split())
    ru.pos = (r-1, c-1)
    board[r-1][c-1] = -1

    # 산타
    for i in range(P):
        name, r, c = map(int, input().split())
        santa = Santa(name, r-1, c-1)
        santas[i] = santa
        board[r-1][c-1] = name

    # 이름 순 정렬
    santas.sort(key=lambda x:x.name)

#### main ####
N, M, P, C, D = map(int, input().split())
board = [[0 for _ in range(N)] for _ in range(N)]
ru = Rudolf()
santas = [None]*P
T = 1 # 턴 수

### 데이터 입력
input_data()
# pprint('input_data...')
# pprint(board)

for _ in range(M):
    # print('')
    # print(T, 'Turn!!!!')
    ### 루돌프 움직임

    ## 가까운 산타 찾기
    near_san = ru.check_near_santa()
    # pprint('near_santa...')
    # pprint(near_san)

    ## 가까운 방향 찾기
    near_dir = ru.check_direction(near_san)
    # pprint('near_dir...')
    # pprint(near_dir)

    ## 그 방향으로 이동
    ru.move(*near_dir)
    # pprint('ru.move...')
    # pprint(board)

    ### 산타 움직임
    for san in santas:
        # print('santa', san.name, 'turn')
        # 기절, 탈락시 패스
        if san.is_out: continue
        if san.is_sleep:
            # 탈락시에는 현재 턴 확인
            # 깰 수 있는 턴이 아니면 패스
            if san.is_sleep != T:
                continue
            # 꺌 수 있는 턴이면 상태 돌려놓기
            else:
                san.is_sleep = False

        # 루돌프와의 가까운 방향 찾기 (우선순위 확인)
        near_dir = san.check_direction(ru)
        # pprint('near_dir...')
        # pprint(near_dir)

        if near_dir == [-1, -1]:
            continue

        # 그 방향으로 이동
        # print(san.name, 'turn.,,m,,')
        san.move(*near_dir)
        # pprint('san.move...')
        # pprint(board)

    ### 점수 추가
    for san in santas:
        if not san.is_out:
            san.score += 1

    ### 중간 과정 확인
    # turn_result()

    ### 종료 조건 확인
    if is_santa_there():
        T += 1
    else:
        break

#### 정답 출력
for san in santas:
    print(san.score, end=' ')
