'''
24060. <실버 3> 알고리즘 수업 - 병합 정렬 1
https://www.acmicpc.net/problem/24060
'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
flag = False

def merge_sort(p, r):
    global arr
    if p < r and not flag:
        q = (p+r)//2
        # print('p, q, r', p, q, r)
        merge_sort(p, q)
        merge_sort(q+1, r)
        merge(p, q, r)

def merge(p, q, r):
    global arr, cnt, flag
    # print(p, q, q+1, r, arr)
    i, j = p, q+1
    t = 0
    tmp = []
    while i<=q and j<=r:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
    while i<=q:
        tmp.append(arr[i])
        i += 1        
    while j<=r:
        tmp.append(arr[j])
        j += 1    
    # arr[p:r+1] = tmp
    i, t = p, 0
    # print(arr)
    while i<=r:
        arr[i]=tmp[t]
        cnt+=1
        if cnt== K:
            print(arr[i])
            flag = True
            return
        # print(f'cnt: {cnt}, change num: {arr[i]}, arr: {arr}')
        i+=1
        t+=1
    # print(arr)
merge_sort(0, N-1)
# print(arr)

if not flag:
    print(-1)