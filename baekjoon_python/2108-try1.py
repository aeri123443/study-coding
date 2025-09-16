'''
2108. 통계학
https://www.acmicpc.net/problem/2108
'''

N = int(input())
arr = [int(input()) for _ in range(N)]

arr.sort()
# print(arr)
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
print(round(sum(arr)/N))
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
print(arr[N//2])
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
counter = {}
for a in arr:
    if a in counter: counter[a]+=1
    else: counter[a]=1
max_count = max(counter.values())
# print(counter)
# print(max_count)
max_nums = [k for k,v in counter.items() if v==max_count ]
# print(max_nums)
if len(max_nums)==1: print(max_nums[0])
else: print(max_nums[1])
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
print(abs(arr[-1]-arr[0]))