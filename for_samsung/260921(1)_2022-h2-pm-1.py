'''
코드트리 빵: 2022 하반기 오후 1번
https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/codetree-mon-bread/description

문제 분석: 14m 32s
코드 1차 작성: 1h 17m 46s
  - [TC98 TIMEOVER] get_next_to_store에서 cnt = visited[sr][sc]로 하고 cnt-1인 주변을 탐색하고 바로 리턴하도록 구현했었음.
        당연히 for dr, dc in MOVE 중 한 번은 걸릴거라고 생각해서, for문 지나면 그냥 -1 -1 리턴하도록 했는데,
        예외 케이스가 있었고, 이것때문에 -1, -1 리턴하고 이후 무한루프에 빠짐.
        2차 작성 단계에서 해당 부분 캐치 후, next_pos = (INF, INF, INF, INF) 업데이트하는 방식으로 바꿈.
코드 2차 작성: 15m 13s
 - [TC99 Fail] 11분 14초동안 디버깅하며 손으로 풀어봐도 9라는 결과가 나옴. 클로드에게 물어본 결과 조건을 잘못 이해. 이후 바로 수정하여 제출.

코드 3차 작성: 11m 14s

총 소요 시간: 1h 58m 46s
'''

from collections import deque

# =============================================
# 전역 및 클래스
# =============================================
DEBUG = False
INF = float('inf')

N, M = -1, -1
MOVE = [(-1,0), (0,-1), (0,1), (1,0)]

board = []
people = {}

class Person:
    def __init__(self, num, er, ec):
        self.num = num
        # 현재 위치
        self.r = -1
        self.c = -1
        # 가고 싶은 편의점 위치
        self.er = er
        self.ec = ec

# =============================================
# 보조 함수
# =============================================
def input_data():
    global N, M, board, people

    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    for i in range(1, M+1):
        er, ec = map(lambda x: int(x)-1, input().split())
        new_person = Person(i, er, ec)
        people[i] = new_person

# 역 BFS
def find_store_route(person):
    num = person.num
    sr, sc = person.r, person.c
    er, ec = person.er, person.ec
    q = deque([(er, ec)])
    visited = [[-1]*N for _ in range(N)]
    visited[er][ec] = 0

    min_count = INF

    while q:
        cr, cc = q.popleft()

        # 조기탈출
        if visited[cr][cc] >= min_count:
            continue

        for dr, dc in MOVE:
            nr, nc = dr+cr, dc+cc
            if 0<=nr<N and 0<=nc<N and visited[nr][nc] == -1:
                # 0 이상이거나, -num인 경우에만 이동 가능
                # 0 미만인데 -num이 아니면 이동 불가
                if board[nr][nc] < 0:
                    continue

                n_cnt = visited[cr][cc] + 1
                visited[nr][nc] = n_cnt
                if nr==sr and nc==sc:
                    min_count = min(n_cnt, min_count)
                else:
                    q.append((nr, nc))

    return visited

def get_next_to_store(visited, person):
    sr, sc = person.r, person.c
    # cnt = visited[sr][sc]

    next_pos = (INF, INF, INF, INF) # 거리 최소, 방향 최소, 좌표정보

    for d, (dr, dc) in enumerate(MOVE):
        nr, nc = dr+sr, dc+sc
        if 0<=nr<N and 0<=nc<N and visited[nr][nc] != -1:
            next_pos = min(next_pos, (visited[nr][nc], d, nr, nc))


    return next_pos[2], next_pos[3]

# 편의점 -> 베이스캠프
def find_near_camps(person):
    num = person.num
    sr, sc = person.er, person.ec
    q = deque([(sr, sc)])
    visited = [[-1]*N for _ in range(N)]
    visited[sr][sc] = 0

    # 캠프 도착 시, min_count까지 걸린 최소시간 업데이트
    near_camp = (INF, INF, INF) # 거리 최소, 행 최소, 열 최소

    while q:
        cr, cc = q.popleft()
        cnt = visited[cr][cc]

        if cnt >= near_camp[0]:
            continue

        for dr, dc in MOVE:
            nr, nc = dr+cr, dc+cc
            if 0<=nr<N and 0<=nc<N and visited[nr][nc]==-1:
                # 0 이상이거나, -num인 경우에만 이동 가능
                # 0 미만인데 -num이 아니면 이동 불가
                if board[nr][nc] < 0 and board[nr][nc] != -num:
                    continue

                visited[nr][nc] = cnt + 1

                if board[nr][nc] == 1:
                    new_camp = (cnt+1, nr, nc)
                    near_camp = min(new_camp, near_camp)
                else:
                    q.append((nr,nc))

    return near_camp


# =============================================
# 메인 로직
# =============================================
def main():
    input_data()
    # if DEBUG: print()

    t = 0
    while people:
        t += 1

        # ================================
        # 1. 격자 내 모든 사람 이동
        # ================================
        # 격자 내 모든 사람 이동, 편의점 도착한 사람 반환
        arrive_people = set()
        for num, person in people.items():
            # 격자 밖에 있으면 패스
            if person.r == -1: continue

            # bfs로 다음 위치 찾고
            visited = find_store_route(person)
            nr, nc = get_next_to_store(visited, person)
            # if DEBUG: print()
            # 이동
            if nr==person.er and nc==person.ec:
                arrive_people.add(num)
            person.r, person.c = nr, nc

            # if DEBUG: print()

        # ================================
        # 2. 편의점 도착 여부 판단
        # ================================
        # 편의점 도착한 사람이 있으면 people 목록에서 빼고, 편의점 -1 기록
        if arrive_people:
            for num in arrive_people:
                person = people[num]
                board[person.er][person.ec] = -num
                del people[num]

        # 조기 탈출
        if not people:
            break

        # if DEBUG: print()
        
        # ================================
        # 3. t <= M, 편의점과 가장 가까운 캠프 배치
        # ================================
        if t<=M and t in people:
            num = t
            person = people[num]
            # t번 사람, 편의점 기준 가장 가까운 베이스 캠프를 반환
            _, nr, nc = find_near_camps(person)

            # t번 사람 위치 업데이트, -num 처리
            person.r, person.c = nr, nc
            board[nr][nc] = -num

            # if DEBUG: print()
        if DEBUG: print()
        # if t>=1000:
            # print(t)

    print(t)

main()