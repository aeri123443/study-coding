'''
꼬리잡기놀이: 2022 상반기 오후 1번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/tail-catch-play/description

문제 분석: 38m 40s
코드 1차 작성: 2h 12m 13s
'''
from collections import deque
# =======================================
# 전역 및 클래스
# =======================================
DEBUG = False
N, M, K = -1, -1, -1
MOVE = [(0,1), (-1,0), (0,-1), (1,0)]
people_board = []
teams = []

class Team:
    def __init__(self, team_num, head_pos, tail_pos, lines):
        self.team_num = team_num
        self.lines = lines
        self.pos_to_idx = {pos:i for i, pos in enumerate(lines)}

        self.head = self.pos_to_idx[head_pos]
        self.tail = self.pos_to_idx[tail_pos]

        self.reverse = False
        self.len = len(lines)
        self.point = 0

# =======================================
# 보조 함수
# =======================================

def grouping_head_to_tail(visited, board, sr, sc):
    visited[sr][sc] = True
    pos = [(sr, sc)]
    tail = ()

    q = deque([(sr, sc)])

    while q:
        cr, cc = q.popleft()

        for dr, dc in MOVE:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and board[nr][nc] in (2,3):
                if board[nr][nc] == 3 and (cr, cc) == (sr, sc):
                    continue                     # visited 찍기 전에 건너뜀
                visited[nr][nc] = True
                pos.append((nr, nc))
                if board[nr][nc] == 3:
                    return pos, (nr, nc)
                q.append((nr, nc))

    return pos, pos[-1]

def grouping_after_tail(visited, board, sr, sc):
    visited[sr][sc] = True
    pos = []
    q = deque([(sr, sc)])

    while q:
        cr, cc = q.popleft()

        for dr, dc in MOVE:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and board[nr][nc]==4:
                visited[nr][nc] = True
                q.append((nr, nc))
                pos.append((nr, nc))

    return pos

def input_data():
    global N, M, K, people_board, teams

    N, M, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    people_board = [[0]*N for _ in range(N)]
    visited = [[False]*N for _ in range(N)]

    team_num = 1
    teams = [None]

    for r in range(N):
        for c in range(N):
            if not visited[r][c] and board[r][c] == 1:
                # 일단 전체 라인 배열, head_pos, tail_pos 반환
                head_pos = (r, c)
                # 머리 -> 꼬리 위치 반환
                line_head_to_tail, tail_pos =  grouping_head_to_tail(visited, board, r, c)
                # 꼬리 -> 라인 끝 위치 반환 (단, 꼬리의 취치는 포함하지 않음)
                line_after_tail = grouping_after_tail(visited, board, *tail_pos)
                lines = [*line_head_to_tail, *line_after_tail]
                # team 추가
                new_team = Team(team_num, head_pos, tail_pos, lines)
                teams.append(new_team)
                for lr, lc in line_head_to_tail:
                    people_board[lr][lc] = team_num
                team_num += 1

def move_team(team):
    team_num, h_idx, t_idx, lines, team_reversed = team.team_num, team.head, team.tail, team.lines, team.reverse
    tr, tc = lines[t_idx]
    line_len = len(lines)

    if not team_reversed:
        n_h_idx = (h_idx-1)%line_len
        n_t_idx = (t_idx-1)%line_len
    else:
        n_h_idx = (h_idx+1)%line_len
        n_t_idx = (t_idx+1)%line_len


    nhr, nhc = lines[n_h_idx]
    people_board[tr][tc] = 0
    people_board[nhr][nhc] = team_num

    team.head = n_h_idx
    team.tail = n_t_idx

def get_receive_team(k):
    got_team = {}
    explore_d = (k//N)%4
    if explore_d == 0:
        r = k%N
        for c in range(N):
            if people_board[r][c] != 0 and not people_board[r][c] in got_team:
                got_team[people_board[r][c]] = (r,c)
                break

    elif explore_d == 1:
        c = k % N
        for r in range(N-1, -1, -1):
            if people_board[r][c] != 0 and not people_board[r][c] in got_team:
                got_team[people_board[r][c]] = (r, c)
                break

    elif explore_d == 2:
        r = N - k%N - 1
        for c in range(N-1, -1, -1):
            if people_board[r][c] != 0 and not people_board[r][c] in got_team:
                got_team[people_board[r][c]] = (r,c)
                break

    elif explore_d == 3:
        c = N - k % N - 1
        for r in range(N):
            if people_board[r][c] != 0 and not people_board[r][c] in got_team:
                got_team[people_board[r][c]] = (r, c)
                break

    return got_team

def get_receive_idx(team, receive_pos):
    team_num, line_len = team.team_num, team.len

    # head 인덱스
    h_idx = team.head
    # 맞은 사람의 인덱스
    r_idx = team.pos_to_idx[receive_pos]

    # 리버스 여부에 따라 몇 번째인지 반환
    if not team.reverse:
        return (r_idx-h_idx) % line_len + 1
    else:
        return (h_idx-r_idx) % line_len + 1


# =======================================
# 메인 로직
# =======================================
def main():
    input_data()
    # if DEBUG: print()

    for k in range(K):
        # =====================
        # 1. 방향대로 1칸 이동
        # =====================
        for t_num in range(1, M+1):
            team = teams[t_num]
            move_team(team)
        # if DEBUG: print()

        # =====================
        # 2. 라운드 공 던지기
        # =====================
        receive_team = get_receive_team(k)

        for team_num, receive_pos in receive_team.items():
            team = teams[team_num]
            # 공을 맞은 사람이 각 팀의 몇 번째 사람인지 확인 후
            receive_idx = get_receive_idx(team, receive_pos)

            # 점수 얻고 반전
            team.point += receive_idx**2
            team.head, team.tail = team.tail, team.head
            team.reverse = not team.reverse

        # if DEBUG: print()

    # 점수 합산 및 출력
    answer = 0
    for team_num in range(1, M+1):
        answer += teams[team_num].point
    print(answer)

main()