'''
84512. lv2 모음사전
https://school.programmers.co.kr/learn/courses/30/lessons/84512
'''

def solution(word):
    alpha_idx = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    n = len(word)

    memo = [1, 5, 5**2, 5**3, 5**4] # 5^0 ~ 5^4 미리 계산
    # print(memo)
    answer = 0

    for i in range(1, n+1):
        answer+=1
        target = word[i-1]

        # print(sum(memo[:6-i]), alpha_idx[target])
        answer += ( sum(memo[:6-i]) * (alpha_idx[target]) )
        # print(i, target, answer)

    return answer

print()
print(solution("A"))
print(1)

print()
print(solution("AA"))
print(2)

print()
print(solution("AAAAE"))
print(6)

print()
print(solution("AAAE"))
print(10)

print()
print(solution("I"))
print(1563)

print()
print(solution("EIO"))
print(1189)

# print()
# print(solution())
# print()

# print()
# print(solution())
# print()
