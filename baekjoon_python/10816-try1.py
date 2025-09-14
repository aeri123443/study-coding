'''
10816. 숫자 카드 2 
https://www.acmicpc.net/problem/10816
'''

N = int(input())
arrN = list(map(int, input().split()))
M = int(input())
arrM = list(map(int, input().split()))

obj = {v:0 for v in arrM}
answer = []

for x in arrN:
    if x in obj:
        obj[x]+=1
for x in arrM:
    answer.append(obj[x])

print(*answer, sep=' ')
