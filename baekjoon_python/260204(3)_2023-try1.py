'''
2023. <골드 5> 신기한 소수
https://www.acmicpc.net/problem/2023
'''

import sys
import math
input = sys.stdin.readline

N = int(input())

# 소수 판별 함수
def isprime(num):
    # 2는 소수임
    if num==2: return True
    # 1과 짝수는 소수가 아님
    if num==1 or num%2==0: return False
    # 1과 자기 자신 외의 숫자로 나누어떨어지면 소수가 아님
    for i in range(3, math.floor(math.sqrt(num))+1, 2):
        if num%i==0: return False
    return True

# 1~N까지 탐색
# 이전 자릿수(n-1)의 결과를 기반으로, n
# n:prev_num의 자릿수, prev_num:이전 자릿수의 겨로가
result = []
def dfs(n, prev_num):
    global result

    if n == N: 
        result.append(prev_num)
        return
    
    prev_num *= 10
    # 애초에 0이 붙는 순간 2나 5로 나누어져서 소수가 아님
    for i in range(1, 10):
        target_num = prev_num+i
        if isprime(target_num):
            # print(target_num, 'is prime')
            dfs(n+1, target_num)

dfs(0, 0)
print('\n'.join(map(str, result)))