'''
11650. 좌표 정렬하기
https://www.acmicpc.net/problem/11650
'''

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key=lambda x:x[1])
arr.sort(key=lambda x:x[0])

# print(*arr, sep='\n')
for x in arr:
    print(*x)