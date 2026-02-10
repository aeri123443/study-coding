'''
42883. Lv.2 큰 수 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/42883
28m 40s
'''

def solution(number, k):
    number = list(number)

    stack = []
    cnt = 0
    for i, n in enumerate(number):
        if stack and n > stack[-1]:
            while stack and n > stack[-1] and cnt < k:
                stack.pop()
                cnt += 1

            if cnt==k:
                stack.extend( number[i:] )
                break
        stack.append(n)
        # print(i, n, stack)

    return ''.join(stack if cnt==k else stack[:cnt-k]) 

print()
print(solution("1924", 2))
print("94")

print()
print(solution("1231234", 3))
print("3234")

print()
print(solution("4177252841", 4))
print("775841")

print()
print(solution("87654321", 3))
print("87654")

print()
print(solution("87654121", 3))
print("87654")