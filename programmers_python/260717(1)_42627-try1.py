'''
42627. 디스크 컨트롤러
https://school.programmers.co.kr/learn/courses/30/lessons/42627

문제 분석: 8m 11s
코드 작성: 21m 30s
디버깅: 0m 0s
total: 29m 41s
'''
import heapq

def solution(jobs):
    jobs_with_idx = [(l, s, idx) for idx, [s, l] in enumerate(jobs)] # (소요시간, 요청시간, 작업 번호)
    jobs_with_idx.sort(key=lambda x:-x[1]) # 작업 요청 시간 역순 정렬 (pop으로 시간복잡도 최소화)

    q = []
    t = 0
    total = 0 # 반환시간 총합
    while jobs_with_idx:
        # 요청 시간이 t 이전인 작업들을 pop하고 대기 큐에 push
        while jobs_with_idx and jobs_with_idx[-1][1] <= t:
            heapq.heappush(q, jobs_with_idx.pop())

        # 요청 처리
        if q:
            l, s, idx = heapq.heappop(q)
            t += l # 처리 후 현재 시간
            total += (t-s) # 반환 시간 계산
            # print("처리 완료: ", idx, s, l, "| 현재 시간: ", t)
        else: # 대기 큐가 없는데 jobs_with_idx가 남아 있을 경우, 해당 요청 시간으로 시간 조정
            t = jobs_with_idx[-1][1]

    # 대기큐에 작업이 남아있을 경우 처리
    while q:
        l, s, idx = heapq.heappop(q)
        t += l  # 처리 후 현재 시간
        total += (t - s)  # 반환 시간 계산
        # print("처리 완료: ", idx, s, l, "| 현재 시간: ", t)

    return total // len(jobs)

print(solution([[0, 3], [1, 9], [3, 5]])) # 8
print(solution([[0, 3], [5, 4], [6, 4]])) # 4
