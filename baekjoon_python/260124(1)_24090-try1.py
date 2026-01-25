'''
24090. <실버 5> 알고리즘 수업 - 퀵 정렬 1
https://www.acmicpc.net/problem/24090
'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
# print(arr)

# start_idx부터 end_idx까지 퀵 정렬
def quick_sort(s_idx, e_idx):
    global arr, cnt
    if cnt == K:
        return
    if s_idx >= e_idx:
        return

    # print('\n >> quick_sort', s_idx, e_idx)

    # i는 작은 놈들만 품어줌 (i가 지나친 자리의 값들은 언제나 pivot보다 작음)
    # j는 그걸 탐색해주는 놈
    pivot = arr[e_idx]
    i = s_idx - 1
    for j in range(s_idx, e_idx):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            cnt += 1
            if cnt == K:
                print(arr[i], arr[j])
                return
            # print(cnt, arr[j], arr[i], arr)
    arr[e_idx], arr[i+1] = arr[i+1], arr[e_idx]
    cnt += 1
    # print(cnt, arr[j], arr[i+1], arr)
    if cnt == K:
        print(arr[i+1], arr[e_idx])
        return
    # 분할
    i+=1
    # print('fixed...', f'arr[{i}]: {arr[i]}')
    # print('part:', s_idx, i-1, '|', i+1, e_idx)

    # quick_sort(s_idx, i-1)
    # quick_sort(i+1, e_idx)

    return -1

result = quick_sort(0, N-1)
if result==-1:
    print(-1)
