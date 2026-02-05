'''
10816. <실버 4> 숫자 카드 2
https://www.acmicpc.net/problem/10816
'''

import sys
from pprint import pprint
from collections import Counter

input = sys.stdin.readline

_ = input()
obj = Counter(map(int, input().split()))
# pprint(obj)

_ = input()
arr = list(map(int, input().split()))

for x in arr:
    print(obj[x] if x in obj else 0, end=' ')
