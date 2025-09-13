'''
2609. 최대공약수와 최소공배수
https://www.acmicpc.net/problem/2609
'''

a, b = map(int, input().split())

def sol(big, small):
    anwer1=1
    extra=small
    for i in range(small, 0, -1):
        # print(small%i)
        if big%i==small%i==0:
            anwer1=i
            extra = small//anwer1
            break
    return [anwer1, extra*big]

if a>b: answer = sol(a, b)
else: answer = sol(b,a)

print(*answer, sep='\n')