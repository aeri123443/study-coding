'''
택배 하차: 2025 하반기 오전 1번 문제
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/delivery-service/description

문제 분석: 14m 07s
코드 작성: 2h 05m 51s
  - 시간 소요 포인트
    - 좌우 하차 후 하강할 때, 재귀 쓰고 싶지 않아서 다른 방법들 한참 고민하다가 결국 재귀(find_down_candidate) 씀...
최종 디버깅: 20m 40s
  - 틀린 포인트
    - find_down_candidate에서 처음엔 if not tmp_set: return을 써서 빠져나오게 하는 바람에, new_candidate_set를 더 탐색하지 않음
      -> if tmp_set으로 변경

총 소요 시간: 2h 40m 40s
'''
from pprint import pprint
from collections import defaultdict

######################################################
#### 클래스 및 전역 변수
######################################################
class Item:
    def __init__(self, k, h, w, c):
        self.num = k
        self.h = h
        self.w = w
        self.r = -1 # 디버깅: 초깃값 -1 괜찮은지?
        self.c = c

INF = float('inf')
N, M = -1, -1
board = []
remain_items = set() # 격자 내 남은 택배 번호
items = {} # 전체 아이템 리스트 (M+1)
######################################################
#### 보조 함수
######################################################

## 보드에서 택배를 제거
def remove_item_from_board(item):
    sr, sc, w, h = item.r, item.c, item.w, item.h

    for r in range(sr, sr+h):
        for c in range(sc, sc+w):
            board[r][c] = 0

## 보드에서 택배를 추가(이동)
def add_item_from_board(item, sr, sc):
    num, w, h = item.num, item.w, item.h

    for r in range(sr, sr+h):
        for c in range(sc, sc+w):
            board[r][c] = num

    item.r, item.c = sr, sc

## 하강 좌표 반환: 어디까지 하강할 수 있는지
def find_down_item(item):
    sr, sc = item.r, item.c
    er, ec = sr+item.h-1,  sc+item.w-1
    result_er = er

    # 택배 바닥 기준, 다음줄에 아무것도 없는지 확인
    for nr in range(er+1, N):
        flag = False
        for nc in range(sc, ec+1):
            if board[nr][nc] != 0:
                flag = True
                break
        # 다음줄에 뭔가 하나라도 있다면, 하강을 멈춤
        if flag:
            return result_er
        else:
            result_er = nr # 여기까진 가능!

    return result_er

## 택배 하강
def down_item(item):
    target_er = find_down_item(item)
    # print()

    # 기존 택배 위치를 제거
    # 단, 초기의 택배 투입 단계(item.r==-1)에서는 넘어감
    if item.r >= 0:
        remove_item_from_board(item)

    # 택배 위치 업데이트
    add_item_from_board(item, target_er-item.h+1, item.c)

# 왼쪽 사이드에 있는 택배들과, 각 택배의 w 값을 비교 -> 택배 번호가 작은 것을 반환
def find_left_side():
    side_list = defaultdict(int) # 각 아이템이 좌측 사이드에 몇 개 있는지 반환

    # 왼쪽 -> 오른쪽 비교
    for r in range(N):
        for c in range(N):
            if board[r][c] > 0:
                side_list[board[r][c]] += 1
                break

    return side_list

# 오른쪽 사이드에 있는 택배들과, 각 택배의 w 값을 비교 -> 택배 번호가 작은 것을 반환
def find_right_side():
    side_list = defaultdict(int) # 각 아이템이 우측 사이드에 몇 개 있는지 반환

    # 오른쪽 -> 왼쪽 비교
    for r in range(N):
        for c in range(N-1, -1, -1):
            if board[r][c] > 0:
                side_list[board[r][c]] += 1
                break

    return side_list

# 사이드에 있는 택배들 중 꺼낼 수 있는 택배를 탐색한 후, 가장 낮은 번호를 탐색하고, 해당 번호를 제거
def out_side_item(answer, side_info):
    target_num = INF

    # 꺼낼 수 있는 택배 중 가장 낮은 번호 탐색
    for k, v in side_info.items():
        item = items[k]
        if item.h == v:
            target_num = min(target_num, k)

    # print(target_num)

    # 해당 택배를 제거
    item = items[target_num]
    remove_item_from_board(item)
    remain_items.remove(target_num)
    answer.append(str(target_num))

    return target_num

# 하강할 가능성이 있는 택배들을 반환
def find_down_candidate(candidate_set, new_candidate_set):

    for num in new_candidate_set:
        item = items[num]
        sr, sc, w, h = item.r, item.c, item.w, item.h

        tmp_set = set()
        # 택배 윗부분 기준, 위로 올라가면서, 가장 먼저 만난 택배를 반환
        for r in range(sr-1, -1, -1):
            flag = False
            for c in range(sc, sc+w):
                if board[r][c] > 0:
                    flag = True
                    tmp_set.add(board[r][c])
            if flag: break

        if tmp_set:
            candidate_set.update(tmp_set)
            find_down_candidate(candidate_set, tmp_set)

# 하강 후보 택배들을 아래에 있는 순서대로 정렬
def sort_down_candidate(candidate_set):
    candidate_list = [ ]
    for num in candidate_set:
        item = items[num]
        r, h = item.r, item.h
        candidate_list.append( (r+h-1, num) )

    candidate_list.sort(key=lambda x:(-x[0]))

    return [ num for r, num in candidate_list]

    # 사이드 하차 후 하강
def down_after_out(out_item_num):
    candidate_set = set()
    find_down_candidate(candidate_set, {out_item_num})
    # 하강 후보 택배들을 아래에 있는 순서대로 정렬
    sorted_candidate_list = sort_down_candidate(candidate_set)
    # 하강
    for num in sorted_candidate_list:
        item = items[num]
        down_item(item)

######################################################
#### 메인 로직
######################################################
def main():
    global N, M, board, items, remain_items
    answer = []

    # 0단계: 기본 데이터 입력
    N, M = map(int, input().split())
    board = [ [0]*N for _ in range(N) ]

    # 1단계: 택배 투입
    for _ in range(M):
        k, h, w, c = map(int, input().split())
        c -= 1

        item = Item(k, h, w, c)
        remain_items.add(k)
        items[k] = item

        ## 하강
        down_item(item)
    # print()

    while remain_items:
        # 2단계: 택배 하차(좌)
        left_side = find_left_side()
        # 좌측 사이드 택배 하차
        out_item_num = out_side_item(answer, left_side)
        # 사이드 하차 후 하강
        down_after_out(out_item_num)
        # print()

        if not remain_items: break

        # 3단계: 택배 하차(우)
        right_side = find_right_side()
        # 우측 사이드 택배 하차
        out_item_num = out_side_item(answer, right_side)
        # 사이드 하차 후 하강
        down_after_out(out_item_num)
        # print()

    # 4단계: 출력
    print('\n'.join(answer))

if __name__ == '__main__':
    main()