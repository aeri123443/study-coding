'''
1차원 폭발 게임
https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-The-1D-bomb-game/

문제 분석: 8m 38s
코드 1차 작성: 22m 34s
최종 디버깅: 17m 43s
  - [TC fail] 끝처리를 복붙하고 수정하는 과정에서, 위에 있는 코드는 수정해놓고 아래 코드를 수정하지 않는 바람에 아래 코드에서 문제가 발생
  - [TC fail]  j-i >= M 만 처리하고, 그렇지 않은 경우 그냥 i+=1 j+=1로 넘어가도록 해서 포인터가 엇나감

총 소요 시간: 48m 56s
'''

#### 전역 선언
N, M = -1, -1

#### 보조
def input_data():
    global N, M
    N, M = map(int, input().split())
    arr = [int(input()) for _ in range(N)]
    return arr

# 투포인터
def bomb(arr):
    l = len(arr)
    if l<2: return False

    flag = False

    i, j = 0, 1
    while j < l:
        if arr[i] == arr[j]:
            j += 1
        else:
            if j-i >= M:
                flag = True
                for k in range(i, j):
                    arr[k]=0
            # print()
            # i+=1
            i = j
            j += 1

    # print()
    # 끝처리
    if j - i >= M:
        flag = True
        for k in range(i, j):
            arr[k] = 0
    # print()
    return flag

#### 메인
def main():
    arr = input_data()
    # print()
    if M == 1:
        print(0)
        return

    while True:
        flag = bomb(arr)
        # print()

        if not flag: break
        arr = [x for x in arr if x > 0]
        # print()

    print(len(arr))
    print('\n'.join(map(str, arr)))

main()
