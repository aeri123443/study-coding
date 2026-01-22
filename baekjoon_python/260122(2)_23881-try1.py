'''
23881. <브론즈 1> 알고리즘 수업 - 선택 정렬 1
https://www.acmicpc.net/problem/23881
'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

def selection_sort():
    cnt = 0
    for i in range(N-1):
        target_num = arr[N-i-1]

        # 최댓값과 그때의 인덱스 찾기
        max_idx, max_num = -1, -1
        for j in range(N-i):
            if max_num < arr[j]:
                max_idx, max_num = j, arr[j]
        # print('max_idx, max_num', max_idx, max_num)

        # swap
        if target_num != max_num:
            arr[N-i-1], arr[max_idx] = arr[max_idx], arr[N-i-1]
            cnt += 1
            # print(f'{cnt}번 교환됨: {arr}, {arr[max_idx], arr[N-i-1]}')
        
        if cnt == K: return f'{arr[max_idx]} {arr[N-i-1]}' 
        # print(cnt, arr)
    return -1
   
print( selection_sort() )