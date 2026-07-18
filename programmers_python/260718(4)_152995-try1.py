'''
152995. 인사고과
https://school.programmers.co.kr/learn/courses/30/lessons/152995
'''

def solution(scores):
    target_total = sum(scores[0])
    sorted_scores = [(i, a, b) for i, [a, b] in enumerate(scores)]
    sorted_scores.sort(key=lambda x:(-x[1], x[2]))

    # 단조 증가
    stack = [] # (a, b_max)
    del_set = set()
    for i, a, b in sorted_scores:
        # 스택이 비어 있으면 추가
        if not stack:
            stack.append( (a,b) )
        # stack에 남아있는 a의 점수가 같다면, b는 어차피 더 커질테니 덮어씌움
        elif stack[-1][0] == a:
            stack[-1] = (a,b)
        # stack에 남아있는 a의 점수가 다르다면, b는 이전 b 점수보다 커야 인사고과를 받을 수 있음
        elif stack[-1][1] <= b:
            stack.append((a, b))
        # 그렇지 않으면 인사고과를 받을 수 없음
        else:
            del_set.add(i)

    # 철수 등급 확인
    if 0 in del_set: return -1

    answer = 1
    for i, a, b in sorted_scores:
        if i in del_set: continue
        if a+b > target_total: answer+=1

    return answer

print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]])) #4