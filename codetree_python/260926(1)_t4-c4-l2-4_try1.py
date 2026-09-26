'''
4가지 연산을 이용하여 1 만들기
https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-make-one-using-four-operations/description
'''
from collections import deque

INF = float('inf')
N = int(input())
max_len = 3*N+1

dp = [INF]*max_len
q = deque([N])
dp[N] = 0

def check_and_push(cn, nn):
    if 0 < nn < max_len and dp[nn] > dp[cn]+1:
        dp[nn] = dp[cn]+1
        q.append(nn)

while q:
    num = q.popleft()

    check_and_push(num, num+1)
    check_and_push(num, num-1)
    if num%2==0 : check_and_push(num, num//2)
    if num%3==0 :check_and_push(num, num//3)

print(dp[1])




