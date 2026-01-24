'''
24090. <실버 5> 알고리즘 수업 - 퀵 정렬 1
https://www.acmicpc.net/problem/24090

깝치지 않고 의사코드가 하란대로 하기...
'''

import sys
sys.setrecursionlimit(int(1e4)) 
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
# print(arr)

def quick_sort(A, p, r):
    # print('quick_sort...', A, p, r)
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)

def partition(A, p, r):
    global cnt

    # print('partition', A, p, r)
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j]<=x:
            i+=1
            A[i], A[j] = A[j], A[i]
            # print(A[i], A[j], arr)
            cnt += 1
            if cnt==K:
                print(A[i], A[j])

    if i+1 != r:
        A[i+1], A[r] = A[r], A[i+1]
        # print( A[i+1], A[r], arr)
        cnt+=1
        if cnt==K:
            print(A[i+1], A[r])
    
    return i+1

quick_sort(arr, 0, len(arr)-1)

if cnt < K:
    print(-1)