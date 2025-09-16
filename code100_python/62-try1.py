'''
p.593 62. 배열 조회하기
소요시간: 25m 00s
'''
import pprint

def solution(arr, n):
    N = len(arr)
    answer = [[0]*N for _ in range(N)]

    for _ in range(n):
        for b in range(N):
            for a in range(N):
                answer[b][N-1-a] = arr[a][b]
        for b in range(N):
            for a in range(N):
                arr[a][b] = answer[a][b]
        
    return answer
# // [
# //   [13, 9, 5, 1],
# //   [14, 10, 6, 2],
# //   [15, 11, 7, 3],
# //   [16, 12, 8, 4]
# // ]
pprint.pprint(solution([
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [13, 14, 15, 16]
    ],
    1))

# // [
# //   [16, 15, 14, 13],
# //   [12, 11, 10, 9],
# //   [8, 7, 6, 5],
# //   [4, 3, 2, 1]
# // ]
pprint.pprint(solution(   [
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [13, 14,15,16]
    ],
    2))