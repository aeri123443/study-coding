'''
12909. 올바른 괄호
https://school.programmers.co.kr/learn/courses/30/lessons/12909

문제 분석 + 코드 작성: 4m 29s
total: 4m 29s
'''


def solution(s):

    if len(s) % 2 != 0 : return False
    s_list = list(s)

    stack = 0
    for x in s_list:
        if x == '(':
            stack += 1
        elif stack > 0:
            stack -= 1
        else:
            return False
    return True if stack == 0 else False

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
print(solution("(())("))
