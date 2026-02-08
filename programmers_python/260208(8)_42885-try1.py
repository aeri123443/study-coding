'''
42885. lv2 구명보트
https://school.programmers.co.kr/learn/courses/30/lessons/42885
틀림
'''



def solution(people, limit):
    n = len(people)
    people_sorted =  sorted(people, reverse=True)
    visited = [False]*n
    answer = 0

    def boat(lm):
        nonlocal visited

        # 어차피 몸무게는 40 이하이므로, 그 이하의 몸무게가 나올 리가 없음
        if lm < 40:
            return
        
        for i in range(n):
            if not visited[i] and lm-people[i]>=0:
                visited[i] = True
                boat(lm-people[i])

    for i in range(n):
        if not visited[i]:
            answer += 1
            visited[i] = True
            boat(limit-people_sorted[i])

    return answer

print()
print(solution([70, 50, 80, 50], 100))
print(3)

print()
print(solution([70, 80, 50], 100))
print(3)


# print()
# print(solution())
# print()