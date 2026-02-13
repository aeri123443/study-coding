'''
1700. <골드 1> 멀티탭 스케줄링
https://www.acmicpc.net/problem/1700
'''

import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, K = map(int, input().split())
items = list(map(int, input().split()))
remains = defaultdict(deque)

for i in range(K):
    v = items[i]
    remains[v].append(i)
# print(remains)

tap = set()
answer = 0
for item in items:
    remains[item].popleft()

    if item in tap:
        continue
    
    if len(tap) < N :
        tap.add(item)
        continue

    remove_target = None
    remove_idx = -1
    for target in tap:
        if not remains[target]:
            remove_target = target
            break

        if remove_idx < remains[target][0]:
            remove_idx = remains[target][0]
            remove_target = target


    tap.remove(remove_target)
    tap.add(item)
    answer+=1

print(answer)