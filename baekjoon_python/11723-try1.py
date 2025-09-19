'''
11723. 집합
https://www.acmicpc.net/problem/11723
'''
import sys
input = sys.stdin.readline

N = int(input())
S = set()

for _ in range(N):
    X = input().split()
    # add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
    if X[0] == 'add': 
        S.add(int(X[1]))
    # remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
    elif X[0] == 'remove': 
        if int(X[1]) in S: 
            S.remove(int(X[1]))
    # check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
    elif X[0] == 'check': 
        if int(X[1]) in S: 
            print(1)
        else: 
            print(0)
    # toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
    elif X[0] == 'toggle': 
        if int(X[1]) in S: 
            S.remove(int(X[1]))
        else: 
            S.add(int(X[1]))
    # all: S를 {1, 2, ..., 20} 으로 바꾼다.
    elif X[0] == 'all': 
        S = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    # empty: S를 공집합으로 바꾼다.
    elif X[0] == 'empty': 
        S = set()

