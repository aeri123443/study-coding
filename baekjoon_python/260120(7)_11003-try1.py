'''
11003. <골드 1> 최솟값 찾기
https://www.acmicpc.net/problem/11003
나중에 모노톤 큐로 풀어보기
'''

from pprint import pprint
import sys
import heapq

input = sys.stdin.readline

N, L = map(int, input().split())
arr = list(map(int, input().split()))

# print(arr)

heap = []
sliding_counter = {}
answer_arr = []

for i in range(N):
    s_idx = max(i-L+1, 0)
    e_idx = i
    # print('s_idx, e_idx', s_idx, e_idx)

    # s_idx가 1 이상으로 가면, 앞 인덱스를 빼야 함.
    if s_idx>0:
        sliding_counter[ arr[s_idx-1] ] -= 1

    # e_idx 값 넣기
    if arr[e_idx] in sliding_counter:
        sliding_counter[ arr[e_idx] ] += 1
    else:
        sliding_counter[ arr[e_idx] ] = 1

    heapq.heappush(heap, arr[e_idx])

    # 최소값 빼야하는데...
    # 최소값이 0이면 pop (최소값이 나올 때까지!)
    # pprint(sliding_counter)
    while heapq:
        if sliding_counter[ heap[0] ] > 0:
            # print('최소:', heap[0])
            answer_arr.append(str(heap[0]))
            break
        else:
            heapq.heappop(heap)

print(' '.join(answer_arr))
