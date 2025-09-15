'''
1929. 소수 구하기
https://www.acmicpc.net/problem/1929
'''

from math import sqrt
M, N = map(int, input().split())

# 소수: 1과 자기자신 외에는 약수가 없는 수
def is_prime(n):
    for i in range(2, int(sqrt(n))+1):
        if n%i==0: return False
    return True

for i in range(M, N+1):
    if i==1: continue
    elif i==2: print(i)
    # 짝수 제외
    elif i%2==0: continue
    else:
        if is_prime(i): print(i)
