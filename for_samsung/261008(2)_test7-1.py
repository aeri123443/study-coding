# 문제 1회독 및 이해 8:3
# 문제 2회독 4:24
# 설계 22:9
# 설계 점검(상태가 크게 변하진 않는듯) 3:33

# 케이스 확인
# - 아예 벽이 막혀있는 경우 -> -1 -> 확인완료
# - 방향만 충분하면 갈 수 있는데 그에 맞는 패턴이 주어지지 못한 경우 -> -1 -> 확인완료

# [!] 턴을 다룰 때마다 T로 잘 나눴는지 확인

from collections import deque

# 전역 관리
N = int(input())
board = [list(input()) for _ in range(N)]
T = int(input())
pattern = [tuple(map(int,input().split())) for _ in range(T)]
MOVE = [(-1,0), (0,+1), (+1,0), (0,-1)]
v_depth = T
# 전역 작성 06:46 + 1:11


#     - 최대 거리에 대한 선택지를 큐에 쌓음
#         - 이 패턴에서 어디까지 가능한지 함수 작성 필요
#         - 거리 0, 1, 2 .. 넓혀가면서 장애물, 격자 체크하고, 안되면 최대거리가 아니어도 종료
def next_pos_with_turn(cr, cc, turn): # 13:9, 모듈 검증해보느라 쫌걸림
    pos = []
    p = turn % T
    d, v = pattern[p]
    dr, dc = MOVE[d]

    for i in range(v+1):
        nr, nc = cr+dr*i, cc+dc*i
        if 0<=nr<N and 0<=nc<N and board[nr][nc] == '.':
            pos.append((nr,nc))
        else: break

    return pos


def main(): # bfs # 32:34.. visited 여부 판정을 처음에 next_pos_with_turn에서 해놓고 안되어서 막 디버깅해봣엇음... 밖으로 ㅃ빼니까 되는거 왜그런거지 다시 봐야겠다
    sr, sc, er, ec = map(lambda x: int(x)-1, input().split())

    # visited[r][c][pattern] -> int # 패턴 두 배 - 적어도 한 번은 머무를 수 있도록 함
    visited = [[[-1] * v_depth for _ in range(N)] for _ in range(N)]
    visited[sr][sc][0] = 0
    # q: r, c, turn
    q = deque([(sr, sc, 0)])

    while q:
        cr, cc, turn = q.popleft()

        next_pos = next_pos_with_turn(cr, cc, turn)
        # print()
        for nr, nc in next_pos:
            if (nr,nc) == (er,ec):
                print(turn+1)
                return
            if visited[nr][nc][(turn+1)%v_depth] == -1 :
                q.append((nr, nc, turn+1))
                visited[nr][nc][(turn+1)%v_depth] = turn+1


    print(-1)

# 케이스 점검: 2:44
# 총 소요시간 1:34:34

main()