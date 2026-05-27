'''
42578. 의상
https://school.programmers.co.kr/learn/courses/30/lessons/42578

31m 14s
'''
from collections import defaultdict

def solution(clothes):
    clothes_map = defaultdict(int)

    for v, k in clothes:
        clothes_map[k] += 1

    answer = 1
    for cv in clothes_map.values():
        answer *= (cv+1)
    return answer - 1

# 5
print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
# 3
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
print(solution([['a1', 'A'], ['a2', 'A'],
                ['b1', 'B'], ['b2', 'B'], ['b3', 'B'],
                ['c1', 'C'], ['c2', 'C'], ['c3', 'C'], ['c4', 'C']]))
print((2+3+4 + 2*3+3*4+2*4 + 2*3*4))
