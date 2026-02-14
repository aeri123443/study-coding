'''
67257. Lv. 2  [카카오 인턴] 수식 최대화
https://school.programmers.co.kr/learn/courses/30/lessons/67257
48m 46s
'''
import re
from collections import deque
from itertools import permutations

# def cal(a,x,b):
#     if x=='+': return a+b
#     if x=='*': return a*b
#     if x=='-': return a-b
    
def solution(expression):
    expression = re.split(r"([-*+])", expression)
    txt = set()

    cal = {
        '+': lambda a,b: a+b ,
        '-': lambda a,b: a-b ,
        '*': lambda a,b: a*b ,
    }

    # 정수화 or 기호 set
    for i, ex in enumerate(expression):
        if ex.isnumeric():
            expression[i] = int(ex)
        else:
            txt.add(ex)
    # print(expression, txt)

    # 우선순위대로 계산하기
    answer = 0    
    for per in permutations(txt):
        q = deque(expression)
        for x in per: # ('+', '-', '*') 순열 순환
            stack = []
            # for i, v in q:
            while q:
                v = q.popleft()
                # print(i)
                if x==v:
                    # stack.append(cal(stack.pop(), x, q.popleft()))
                    stack.append(cal[x](stack.pop(), q.popleft()))
                    
                else:
                    stack.append(v)
            # print(stack)
            q = deque(stack)
        # print(q)
        answer = max(answer, abs(q[0]))
    
    return answer

print()
print(solution("100-200*300-500+20"))
print(60420)

print()
print(solution("50*6-3*2"))
print(300)

# print()
# print(solution())
# print()
