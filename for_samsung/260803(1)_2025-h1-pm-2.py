'''
여왕 개미: 2025 상반기 오후 2번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/queen-ant/description

다시 풀어보기!
'''

####################################################################
##### 전역 선언
####################################################################
Q, N = -1, -1
arr = [0]

####################################################################
##### 보조 함수
####################################################################

### mid 시간 동안 r마리의 개미로 모든 개미집을 커버할 수 있는지 검사
def check(mid, r):
    cnt = 0
    last_covered_x = -1  # 현재 개미가 정찰 가능한 최대 좌표

    for idx in range(1, len(arr)):
        # 1. 철거된 개미집(-1)은 건너뜀
        if arr[idx] == -1:
            continue

        # 2. 현재 개미집 좌표가 기존 개미의 정찰 범위를 벗어난 경우
        if arr[idx] > last_covered_x:
            cnt += 1  # 새로운 개미 배치
            last_covered_x = arr[idx] + mid  # 새 개미의 최대 정찰 범위 갱신

    return cnt <= r


### 이분 탐색 (Parametric Search)
def bs(r):
    i = 0
    j = 10 ** 9  # 개미집 간 최대 거리 범주
    ans = j

    while i <= j:
        mid = (i + j) // 2

        # mid 시간 내에 r마리로 전부 정찰 가능한가?
        if check(mid, r):
            ans = mid
            j = mid - 1  # 최소 시간을 찾기 위해 왼쪽 범위를 더 탐색
        else:
            i = mid + 1  # 불가능하면 시간을 더 늘림

    return ans

####################################################################
##### 메인 로직
####################################################################
def main():
    global Q, N
    Q = int(input())
    answer = []

    for q in range(Q):
        line = list(map(int, input().split()))
        cmd = line[0]

        # 마을 건설
        if cmd == 100:
            N = line[1]
            arr.extend( line[2:]  )
        # 개미집 건설
        elif cmd == 200:
            arr.append(line[1])
        # 개미집 철거
        elif cmd == 300:
            p = line[1]
            arr[p] = -1
        # 개미집 정찰
        elif cmd == 400:
            t = bs(line[1])
            answer.append(t)
        # print()

    print('\n'.join(map(str,answer)))

main()