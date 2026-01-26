'''
42586. 기능개발
https://school.programmers.co.kr/learn/courses/30/lessons/42586
27m 30s
'''

def solution(progresses, speeds):
    N = len(progresses)
    cnt = 0
    done_days = [0]*N

    # 작업 완료일
    day=0
    while cnt<N:
        for i in range(N):
            if progresses[i] >= 100:
                continue

            progresses[i]+=speeds[i]

            if progresses[i] >= 100:
                done_days[i] = day
                cnt += 1
        day+=1
    # print(done_days)

    # 출시일
    answer = [1]
    top_val = done_days[0]
    for i in range(1, N):
        if top_val >= done_days[i]:
           answer[-1] += 1
        else:
            answer.append(1)
            top_val = done_days[i]
    return answer

print()
print(solution([93, 30, 55], [1, 30, 5]))
print([2, 1])

print()
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
print([1, 3, 2])

# 최소최대
print()
print(solution([1], [1]))
print([1])

# 최소최대
print()
print(solution([1], [100]))
print([1])

print()
print(solution([99, 99, 99], [1, 2, 3]))
print([3])

# 경계값
# 가장큰값
# print()
# print(solution())
# print()