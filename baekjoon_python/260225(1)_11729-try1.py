'''
11729. <골드 5> 하노이 탑 이동 순서
https://www.acmicpc.net/problem/11729
'''

import sys
N = int(sys.stdin.readline())

answer = []
# num, from, via, to
def hanoi(num, f, v, t):
    global answer

    if num==1:
        answer.append(f'{f} {t}')
        return
    
    # n-1개를 via에 옮기고
    hanoi(num-1, f, t, v)
    # 가장 큰 것을 to로 옮기고
    answer.append(f'{f} {t}')
    # via에 있던 n-1개를 to로 옮김
    hanoi(num-1, v, f, t)

hanoi(N, 1, 2, 3)
print(len(answer))
print('\n'.join(answer))