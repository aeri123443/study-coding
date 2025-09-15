'''
1966. 프린터 큐
https://www.acmicpc.net/problem/1966
'''

from collections import deque
# import time

for _ in range(int(input())):     
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    max_num = max(arr)

    q = deque()
    for i, v in enumerate(arr):
        q.append([v, i])

    # q.qsize()
    answer = 0
    while q:
        # time.sleep(0.5)
        [target, target_idx] = q.popleft()
        # print(max_num, target, target_idx)
        if target == max_num:
            # print('good')
            answer += 1
            if target_idx == M:
                print(answer)
                break
            arr[target_idx] = -10
            max_num = max(arr)
        else: 
            q.append([target, target_idx])
