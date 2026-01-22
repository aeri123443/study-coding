'''
24051. <브론즈 1> 알고리즘 수업 - 삽입 정렬 1
https://www.acmicpc.net/problem/24051
'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

def insertion_sort():
    cnt = 0
    for i in range(1, N):
        target_num = arr[i]
        j = i - 1

        # 뒤로 밀기
        while j >= 0 and arr[j] > target_num:
            arr[j+1] = arr[j]
            cnt += 1
            if cnt == K:
                return arr[j]
            j -= 1

        # 삽입
        if j + 1 != i:
            arr[j+1] = target_num
            cnt += 1
            if cnt == K:
                return target_num

    return -1

print(insertion_sort())
