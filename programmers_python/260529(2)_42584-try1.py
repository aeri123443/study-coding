'''
42584. 주식 가격
https://school.programmers.co.kr/learn/courses/30/lessons/42584

문제 분석: 8m 17s
코드 작성: 10m 20s
디버깅: 0m 0s
total: 18m 37s
'''

def solution(prices):
    n = len(prices)
    answer = [0]*n
    stack = [] # (idx, value)
    for i, v in enumerate(prices):
        while stack and v < stack[-1][1]:
            rear_idx, _ = stack.pop()
            answer[rear_idx] = i - rear_idx
        stack.append( (i, v) )
        # print(i, v, stack, answer)

    # 남은 스택 처리
    last_idx = n - 1
    for i, _ in stack:
        answer[i] = last_idx - i

    return answer

# [4, 3, 1, 1, 0]
print(solution([1, 2, 3, 2, 3]))
# [7, 5, 1, 3, 2, 1, 1, 0]
print(solution([1, 2, 5, 3, 4, 9, 1, 2]))
