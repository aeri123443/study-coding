'''
23969. <브론즈 1> 알고리즘 수업 - 버블 정렬 2
https://www.acmicpc.net/problem/23969
'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

def bubble_sort():
    global cnt
    for i in range(N-1):
        # print('i...', i)
        for j in range(N-i-1):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
                cnt += 1
                if K == cnt:
                    return ' '.join(map(str, arr))
            # print(j, j+1)
            # print(cnt, arr)
    return -1
   
print( bubble_sort() )