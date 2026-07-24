'''
1차원 젠가
https://www.codetree.ai/ko/trails/complete/curated-cards/intro-jenga-1d/description?open=true

문제 분석: 4m 50s
코드 작성: 15m 28s
  - 시간 소요 포인트
    - 하나씩 밀고 나서 보니 배열 자체가 줄어들어야 하는 문제였고, pop이 더 빠를 것 같아서 pop으로 바꿈
최종 디버깅: 0m 0s

총 소요 시간: 20m 23s
'''

N = int(input())
arr = [int(input()) for _ in range(N)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

def remove_item(s, e):
    for i in range(s, e+1):
        arr[i] = 0

def pop_item(s, e):
    l = e - s + 1
    for _ in range(l):
        arr.pop(s)
s1 -= 1
e1 -= 1
s2 -= 1
e2 -= 1

remove_item(s1, e1)
pop_item(s1, e1)

remove_item(s2, e2)
pop_item(s2, e2)

print(len(arr))
print('\n'.join(map(str, arr)))
