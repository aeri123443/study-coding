'''
1339. <골드 4> 단어 수학
https://www.acmicpc.net/problem/1339
'''

import sys
from pprint import pprint

input = sys.stdin.readline

N = int(input())
tens = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]
weights = {} #가중치

for _ in range(N):
    s = list(input().strip())[::-1]
    for i, c in enumerate(s):
        if c not in weights:
            weights[c] = 0
        
        weights[c] += tens[i]
    # pprint(weights)

sorted_weights = sorted(weights.items(), key=lambda x:x[1])
# print(sorted_weights)

answer = 0
for num in range(9, -1, -1):
    if sorted_weights:
        answer += num * sorted_weights.pop()[1]

print(answer)

# 예외 테케 만들기
# ACBDE 1개, EAAA 9개
# 97658 + (8999)*9
# print(97658 + (8999)*9)
# 178649