'''
11399. ATM
https://www.acmicpc.net/problem/11399
'''
import sys
sys.stdin = open('input.txt')

N = int(input())
p_list = list(map(int, input().split()))

p_list.sort(reverse=True)

answer = 0
for p in range(N, 0, -1):
    answer += p_list[p-1]*p

print(answer)
