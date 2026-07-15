'''
12973. 짝지어 제거하기
https://school.programmers.co.kr/learn/courses/30/lessons/12973

문제 분석: 5m 11s
코드 작성: 4m 30s
디버깅: 0m 0s
total: 9m 41s
'''

def solution(s):
    if len(s) % 2 != 0: return 0

    stack = []
    for c in s:
        if not stack or stack[-1] != c:
            stack.append(c)
        else:
            stack.pop()

    return 0 if stack else 1

print(solution("baabaa")) # 1
print(solution("cdcd"))  #0
print(solution("bbaaaa")) # 1
print(solution("babaacac")) # 0
print(solution("abba")) # 1
print(solution("aa")) # 1
