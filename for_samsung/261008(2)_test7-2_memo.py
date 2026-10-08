# # from collections import deque
# # H, W, R, Q = map(int, input().split())
# # MOVE = [(0,1), (0,-1), (1,0), (-1,0)]
# #
# # shapes = {}
# # # 반지름 좌표 추출
# # def get_shape(r):
# #     visited = {(0,0)}
# #     q = deque([(0, 0)])
# #
# #     while q:
# #         cr, cc = q.popleft()
# #         for dr, dc in MOVE:
# #             ncr, ncc = cr+dr, cc+dc # 새 중심 좌표
# #             if all([((ncr+ddr)**2 + (ncc+ddc)**2) <= r**2 for ddr, ddc in [(-0.5, -0.5), (0.5, 0.5), (0.5,-0.5), (-0.5,0.5)]]) and not (ncr,ncc) in visited:
# #                 q.append((ncr, ncc))
# #                 visited.add((ncr, ncc))
# #     return visited
# #
# # def make_shape_type():
# #     for r in range(1, 10+1):
# #         s = get_shape(r)
# #         shapes[r] = s
# #
# # def add_ball_in_board(num, cr, cc, r):
# #     for dr, dc in shapes[r]:
# #         board[cr+dr][cc+dc] = num
# # make_shape_type()
# #
# # board = [[0]*30 for _ in range(30)]
# # for r in range(9, 0, -1 ):
# #     add_ball_in_board(r, 15, 15, r)
# #
# # for b in board:
# #     print(*b)
# #
# # # 28:24s
# #
# #
# #
# # =====================================================================
#
#
# # 테케 생각해내기 15:25 + 6ㅣ27
#
# board = [
#     [0, a, b, c, 0, 0, 0],
#     [0, 1, 1, 1, 0, 0, 0],
#     [1, 1, 1, 1, 1, 0, 0],
#     [1, 1, 1, 1, 1, 0, 0],
#     [1, 1, 1, 1, 1, 0, 0],
#     [0, 1, 1, 1, 0, 0, 0],
# ]
from collections import deque

N = int(input())
if N == 2:
    print(1)
elif N == 3:
    print(1)
else:
    INF = float('inf')
    dp = [[0] * (N + 1) for _ in range(2)]
    dp[0][2] = 1
    dp[1][3] = 1

    for n in range(4, N + 1):
        dp[0][n] = dp[0][n - 2] + dp[1][n - 2] # 2칸으로 도착한 경우
        dp[1][n] = sum(dp[0][n - 3], dp[1][n - 2])  # 3칸으로 도착한 경우

    print(sum(dp[-1]))