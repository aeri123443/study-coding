'''
12973. lv2 짝지어 제거하기
https://school.programmers.co.kr/learn/courses/30/lessons/12973
8m 12s
'''

def solution(s):
    n = len(s)
    stack = []

    if n%2 != 0: 
        return 0
    
    for x in s:
        if stack and stack[-1]==x:
            stack.pop()
        else:
            stack.append(x)

    return 0 if stack else 1

print()
print(solution('baabaa'))
print(1)

print()
print(solution('cdcd'))
print(0)

print()
print(solution('aabcbbcb'))
print(1)


print()
print(solution('aabcbcbb'))
print(0)