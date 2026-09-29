'''
Sam의 피자학교: 2021 하반기 오후 2번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/sam-pizza-school/

문제 분석 + 코드 1차 작성: 1h 46m 37s
    - 타임랩 찍는거 깜빡했는데... 문제분석 사십몇분정도 걸린듯...??
    - [TC6 error] 5단계 get_sum_board에서 인덱스 에러 -> 디버깅해보니 5단계에서 비정상으로 arr2가 접혀있었음 -> 역추적으로 달팽이 배열 넣는 과정에서 등호 문제가 있었음을 발견
        roll_arr 함수에서 if d==2 and nc => top-1  -->  if d==2 and nc > top-1  변경
코드 2차 작성: 15m 23s

총 소요 시간 2h 2m 0s
'''

# ==========================================
# 전역 선언
# ==========================================
DEBUG = False
N, K = map(int, input().split())
MOVE = [(0,-1), (-1,0), (0,1), (+1,0)]
# ==========================================
# 보조 함수
# ==========================================

def cal_roll_val(arr):
    top = 1
    bottom = N
    height = 1

    while True:
        new_height = top + 1
        new_top = height
        new_bottom = bottom - top
        if new_bottom < new_top:
            break

        height, top, bottom = new_height, new_top, new_bottom

    return top, bottom, height

def roll_arr(arr, top, bottom, height):
    snail = [[-1]*bottom for _ in range(height)]

    d = 0
    cr, cc = height-1, bottom-1
    for i in range(N-1, -1, -1):
        x = arr[i]
        snail[cr][cc] = x
        dr, dc = MOVE[d]
        nr, nc = cr+dr, cc+dc

        if 0<=nr<height and 0<=nc<bottom and snail[nr][nc] == -1:
            if d==2 and nc > top-1:
                d = (d + 1) % 4
                dr, dc = MOVE[d]
                nr, nc = cr + dr, cc + dc

                if not (0<=nr<height and 0<=nc<bottom and snail[nr][nc] == -1):
                    break
        else:
            d = (d+1)%4
            dr, dc = MOVE[d]
            nr, nc = cr + dr, cc + dc
            if not (0<=nr<height and 0<=nc<bottom and snail[nr][nc] == -1):
                break
        cr, cc = nr, nc

    return snail

def get_sum_board(arr, height, width):
    sum_board = [[0]*width for _ in range(height)]

    # 오른쪽, 아래로만 이동
    for r in range(height):
        for c in range(width):
            if arr[r][c] == -1: continue

            for dr, dc in MOVE[:2]:
                nr, nc = r+dr, c+dc
                if 0<=nr<height and 0<=nc<width and arr[nr][nc] != -1:
                    d = abs(arr[nr][nc] - arr[r][c]) // 5
                    if arr[nr][nc] > arr[r][c]:
                        sum_board[nr][nc] -= d
                        sum_board[r][c] += d
                    else:
                        sum_board[r][c] -= d
                        sum_board[nr][nc] += d

    return sum_board

def spread_board(arr, height, width):
    arr1 = []
    for c in range(width):
        for r in range(height-1, -1, -1):
            if arr[r][c] != -1:
                arr1.append(arr[r][c])

    return arr1

def fold_board(arr):
    l = N//4
    a0, a1, a2, a3 = arr[:l], arr[l:l*2], arr[l*2:l*3], arr[l*3:]
    arr2 = [a2[::-1], a1, a0[::-1], a3]

    return arr2

# ==========================================
# 메인 로직
# ==========================================
def main():
    answer = 0

    # =================================
    # 0. 초기 밀가루 정보
    # =================================
    arr1 = list(map(int, input().split()))

    while True:
        answer += 1
        # =================================
        # 1. 밀가루 추가
        # =================================

        min_val = min(arr1)
        for i in range(N):
            if arr1[i] == min_val: arr1[i]+=1

        if DEBUG: print()


        # =================================
        # 2. 도우 말기
        # =================================

        top, bottom, height = cal_roll_val(arr1)
        arr2 = roll_arr(arr1, top, bottom, height)
        if DEBUG: print()

        # =================================
        # 3. 도우 누르기
        # =================================
        sum_board = get_sum_board(arr2, height, bottom)
        for r in range(height):
            for c in range(bottom):
                if arr2[r][c] > -1: arr2[r][c] += sum_board[r][c]

        arr1 = spread_board(arr2, height, bottom)
        if DEBUG: print()

        # =================================
        # 4. 두 번 접기
        # =================================

        arr2 = fold_board(arr1)
        if DEBUG: print()

        # =================================
        # 5. 도우 누르기
        # =================================
        sum_board = get_sum_board(arr2, len(arr2), len(arr2[0]))
        for r in range(len(arr2)):
            for c in range(len(arr2[0])):
                if arr2[r][c] > -1: arr2[r][c] += sum_board[r][c]

        arr1 = spread_board(arr2, len(arr2), len(arr2[0]))
        if DEBUG: print()

        # =================================
        # 6. 밀가루 최대 최소 계산
        # =================================
        if (max(arr1) - min(arr1)) <= K:
            break

    print(answer)

main()