'''
2805. <실버2> 나무 자르기
https://www.acmicpc.net/problem/2805
'''

import sys
input = sys.stdin.readline

N, M = 0, 0
arr = []

# 나무 수 계산
def cal_wood(target):
    global arr
    
    result = 0
    for v in arr:
        if v > target:
            result += (v-target)
    return result

# 값 입력
N, M = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = max(arr)
ans = 0

while left <= right:
    mid = (left + right) // 2
    total = cal_wood(mid)

    if total >= M:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1
        
print(ans)