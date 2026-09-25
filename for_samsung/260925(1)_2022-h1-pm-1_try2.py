'''
꼬리잡기놀이: 2022 상반기 오후 1번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/tail-catch-play/description

문제 분석: 19m 02s
코드 1차 작성: 1h 9m 8s
    - 신경쓴 것: 단계별 디버깅(모듈 단위로 검증)
TC fail 없이 통과.
총 소요 시간: 1h 28m 11s
'''

# ==================================================
# 전역 및 클래스
# ==================================================
DEBUG = False
N, M, K = -1, -1, -1
MOVE = [(0,1), (1,0), (0,-1), (-1,0)]
teams = []
people_board = []

# ==================================================
# 보조 함수
# ==================================================

# 헤드 기준, 팀원 수, 라인 반환
def get_line(board, team_num, hr, hc):
    path = [(hr, hc)]
    cr, cc = hr, hc
    cnt = 1
    visited = {(hr,hc)}
    people_board[hr][hc] = team_num
    while True:
        # print()
        for dr, dc in MOVE:
            nr, nc = cr+dr, cc+dc
            if 0<=nr<N and 0<=nc<N and board[nr][nc] > 0:
                # 1 -> 2
                if board[cr][cc]==1 and board[nr][nc]==2 and (nr, nc) not in visited:
                    path.append((nr, nc))
                    visited.add((nr, nc))
                    people_board[nr][nc] = team_num
                    cnt += 1
                    cr, cc = nr, nc
                    break
                # 2 -> 2||3
                elif board[cr][cc]==2 and board[nr][nc] in (2,3) and (nr, nc) not in visited:
                    path.append((nr, nc))
                    visited.add((nr, nc))
                    people_board[nr][nc] = team_num
                    cnt += 1
                    cr, cc = nr, nc
                    break
                # 3 -> 1(종료) || 4
                elif board[cr][cc] == 3:
                    if board[nr][nc] == 1:
                        return cnt, path
                    elif board[nr][nc] == 4 and (nr, nc) not in visited:
                        path.append((nr, nc))
                        visited.add((nr,nc))
                        cr, cc = nr, nc
                        break
                # 4 -> 1 (종료)
                elif board[cr][cc] == 4:
                    if board[nr][nc] == 4 and (nr, nc) not in visited:
                        path.append((nr,nc))
                        visited.add((nr,nc))
                        cr, cc = nr, nc
                    if board[nr][nc] == 1:
                        return cnt, path

def init_data():
    global N, M, K, teams, people_board

    N, M, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    teams = [[-1,[]]]
    people_board = [[0]*N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if board[r][c]==1:
                team_num = len(teams)
                team_cnt, path = get_line(board, team_num, r, c)
                teams.append([team_cnt, path])

# ==================================================
# 메인 로직
# ==================================================
def main():
    init_data()
    if DEBUG: print()

    answer = 0
    for k in range(K):
        # 1. 머리 사람 따라서 1칸 이동
        for team_num in range(1, M+1):
            member_cnt, path = teams[team_num]
            tr, tc = path[member_cnt-1]
            nr, nc = path.pop()
            if people_board[tr][tc] == team_num: people_board[tr][tc] = 0
            people_board[nr][nc] = team_num
            new_path = [(nr,nc), *path]
            teams[team_num][1] = new_path
        if DEBUG: print()

        # 2. 공 던지기
        a = (k//N)%4
        b = k%N

        if a == 0:
            r = b
            ball_path = [(r,c) for c in range(N)]
        elif a == 1:
            c = b
            ball_path = [(r,c) for r in range(N-1, -1, -1)]
        elif a == 2:
            r = N - b - 1
            ball_path = [(r,c) for c in range(N-1, -1, -1)]
        elif a == 3:
            c = N - b - 1
            ball_path = [(r,c) for r in range(N)]

        # 공을 처음 맞은 사람의 팀과 좌표는
        get_person_pos = None
        get_team = None
        for r, c in ball_path:
            if people_board[r][c] != 0:
                get_person_pos = (r,c)
                get_team = people_board[r][c]
                break

        # 공 맞은 사람이 있으면
        if get_team:
            get_team_member_cnt, get_team_path = teams[get_team]
            # 상대 위치 확인
            people_idx = get_team_path.index(get_person_pos)
            # 점수 얻기
            answer += (people_idx+1)**2
            # 머리-꼬리 반전
            member_path = get_team_path[:get_team_member_cnt]
            other_path = get_team_path[get_team_member_cnt:]
            new_team_path = member_path[::-1] + other_path[::-1]
            teams[get_team][1] = new_team_path

        if DEBUG: print()
    print(answer)
main()