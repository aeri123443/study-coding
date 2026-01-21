'''
2164. <실버 4> 카드2
https://www.acmicpc.net/problem/2164
'''

from pprint import pprint
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
q = deque( [i+1 for i in range(N)] )
# print(q)

while len(q)>1:
    # 첫 녀석 빼고
    q.popleft()
    # 다음 녀석 뒤로 넣기
    q.append(q.popleft())
    # print(q)

print(q.popleft())
