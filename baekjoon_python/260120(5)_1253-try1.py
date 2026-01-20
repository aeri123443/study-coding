'''
1253. <골드 4> 좋다
https://www.acmicpc.net/problem/1253
'''

from pprint import pprint
import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))
arr_set = set(arr)
good_set = set()
# arr_list = list(arr_set)
# print(arr, arr_set, good_set)
arr_counter = Counter(arr)
# print(arr_counter)
# s, e = 0, 1
max_num = max(arr_set)

# 좋은 수 등록
for s in range(N-1):
    for e in range(s+1, N):
        sum_num = arr[s]+arr[e]
        if sum_num > max_num:
            break
        if sum_num in arr_set:
            # 자기 자신이 포함된 경우
            if sum_num in [arr[s], arr[e]]:
                # s와 e값이 다르면 sum_num이 두 개 이상 있으면 됨
                if (arr[s] != arr[e]) and (arr_counter[sum_num]>=2):
                    good_set.add(sum_num)
                # s와 e값이 같으면 sum_num이 세 개 이상 있으면 됨
                elif (arr[s] == arr[e]) and (arr_counter[sum_num]>=3):
                    good_set.add(sum_num)
            else: good_set.add(sum_num)

# good_set.add(arr[s]+arr[e])
# print(good_set)

# 정답 구하기
answer = 0
for x in good_set:
    answer += arr_counter[x]
print(answer)
