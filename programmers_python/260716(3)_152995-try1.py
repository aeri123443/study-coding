'''
152995. 인사고과
https://school.programmers.co.kr/learn/courses/30/lessons/152995

문제 분석: 13m 56s
코드 작성: 25m 33s
디버깅: 25m 22s
total: 1h 6m 51s
'''
def solution(scores):
    # a 내림차순, b 오름차순 정렬 후 단조 증가 스택
    sorted_scores = [(i, a, b) for i, (a, b) in enumerate(scores)]
    sorted_scores.sort(key=lambda x: (-x[1], x[2]))

    stack = [] # (a, b_max)
    out_people = set() # 인사고과 못 받는 사람들
    target_score = -1
    for i, a, b in sorted_scores:
        if not stack:
            stack.append((a, b)) # 합계, 인덱스, 단조증가 기준(b)
        elif stack[-1][0] > a and  stack[-1][1] > b:
            if i == 0 : return -1
            out_people.add(i)
        elif stack[-1][1] == a:
            stack[-1] = (a, b)
        else:
            stack.append((a, b))

        if i == 0:
            target_score = a+b

    # 원호 등수 체크 (원호보다 등수가 높은 사람 수를 카운트)
    answer = 0
    for i, a, b in sorted_scores:
        if i in out_people: continue

        if i!=0 and a+b > target_score:
            answer+=1

    return answer+1

print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]])) # 4
print(solution([[1,1], [1,2], [2,3], [1,3], [3,2]])) # -1
print(solution([[1,5], [2,3], [1,2], [1,4], [3,2]])) # 1
print(solution([[2,3], [1,5], [1,2], [1,4], [3,2]])) # 2
print(solution([[2,6], [1,2]])) # 1
print(solution([[2,6]])) # 1
