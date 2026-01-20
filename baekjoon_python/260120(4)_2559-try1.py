'''
2559. <실버3> 수열
https://www.acmicpc.net/problem/2559
'''

from pprint import pprint
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
# print(arr)

# idx 0~K-1만큼을 먼저 구함
total = sum(arr[0:K])
# print(arr[0:K])
# pprint(total)

s = 0
e = K-1
# print(s, e)

max_num = total
while e < N-1:
    
    e += 1
    total = total + arr[e] - arr[s]
    # print(s, e, arr[s], arr[e], total)
    # print(total)
    s += 1
    max_num = max(max_num, total)
print(max_num)