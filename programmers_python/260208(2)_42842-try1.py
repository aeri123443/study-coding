'''
42842. lv2 카펫
https://school.programmers.co.kr/learn/courses/30/lessons/42842
15m 50s
'''
import math

# yello의 약수 반환
def find_wh(yello):
    wh_list = []
    for i in range(1, math.ceil(yello**0.5)+1):
        if yello%i == 0:
            wh_list.append([yello//i, i])

    return wh_list

def solution(brown, yellow):
    wh_list = find_wh(yellow)

    for w, h in wh_list:
        if not w >= h:
            continue
        if (w+h)*2+4 == brown:
            return [w+2, h+2]
    return []

print()
print(solution(10, 2))
print([4, 3])

print()
print(solution(8, 1))
print([3, 3])

print()
print(solution(24, 24))
print([8, 6])

# print()
# print(solution())
# print()

# 최대최소
# w==h
# 경곘값