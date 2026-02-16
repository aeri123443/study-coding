'''
1644. <골드 3> 소수의 연속합
https://www.acmicpc.net/problem/1644
'''

import sys

N = int(sys.stdin.readline())

### 에라토스테네스의 체
def prime_seive(n):
    # 홀수만 뽑아내기
    prime = [True]*(n+1)
    # 0, 1은 소수가 아님
    prime[0] = prime[1] = False

    for i in range(2, int(n**0.5)+1):
        if prime[i]:
            for j in range(i*i, n+1, i):
                prime[j]=False

    return [i for i in range(n+1) if prime[i]]

if N==1: 
    print(0)
    sys.exit()

# 소수만 뽑아내기
primes = prime_seive(N)
# print(primes)

### 슬라이딩 윈도우
i = j = 0
total = primes[j]
prime_len = len(primes)
cnt = 0

while i<=j:

    if total < N:
        j += 1
        if j>=prime_len: 
            break
        total+=primes[j]

    elif total > N:
        total-=primes[i]
        i += 1

    else: # total == N:
        # print(primes[i],primes[j])
        cnt += 1
        total-=primes[i]
        i += 1

print(cnt)