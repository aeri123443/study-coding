'''
1764. 듣보잡
https://www.acmicpc.net/problem/1764
'''

N, M = map(int, input().split())
set1 = {input() for _ in range(N)}
set2 = {input() for _ in range(M)}

answer = sorted(set1&set2)
print(len(answer))
print(*answer, sep='\n')
