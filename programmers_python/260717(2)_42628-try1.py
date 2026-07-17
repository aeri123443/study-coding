'''
42628. 이중우선순위큐
https://school.programmers.co.kr/learn/courses/30/lessons/42628

문제 분석: 1m 33s
코드 작성: 21m 32s
디버깅: 0m 0s
total: 23m 5s
'''
import heapq

def solution(operations):
    min_q = [] # 최소 힙 (값, idx)
    max_q = [] # 최대 힙
    idx_set = set() # 현재 q에 있는 idx 목록

    for idx, cmd in enumerate(operations):
        c, n = cmd.split(' ')
        n = int(n)
        if c == "I": # 삽입
            heapq.heappush(min_q, (n, idx))
            heapq.heappush(max_q, (-n, idx))
            idx_set.add(idx)
        elif idx_set: # 기타는 삭제 명령, 큐에 데이터가 있을 때만 삭제 수행
            if n == 1: # 최댓값 제거
                while max_q:
                    target_n, target_idx = heapq.heappop(max_q)
                    # 타겟이 idx_set에 있으면 제거 가능, 없으면 D -1 작업에서 제거된 유령 작업임
                    if target_idx in idx_set:
                        idx_set.remove(target_idx)
                        break
            else:  # 최솟값 제거
                while min_q:
                    target_n, target_idx = heapq.heappop(min_q)
                    # 타겟이 idx_set에 있으면 제거 가능, 없으면 D 1 작업에서 제거된 유령 작업임
                    if target_idx in idx_set:
                        idx_set.remove(target_idx)
                        break
        # print(c, n, idx_set)

    # 최솟값, 최댓값 찾기
    if not idx_set: return [0,0]

    max_num, min_num = 0, 0
    while max_q:
        target_n, target_idx = heapq.heappop(max_q)
        if target_idx in idx_set:
            max_num = -target_n
            break
    while min_q:
        target_n, target_idx = heapq.heappop(min_q)
        if target_idx in idx_set:
            min_num = target_n
            break

    return [max_num, min_num]

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])) # [0,0]
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])) # [333, -45]
