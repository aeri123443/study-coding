'''
42578. 의상
https://school.programmers.co.kr/learn/courses/30/lessons/42578

문제 분석: 0m 54s
코드 작성: 4m 4s
디버깅: 0m 0s
total: 4m 58s
'''
from collections import defaultdict

def solution(clothes):
    clothe_dict = defaultdict(int)

    for _, k in clothes:
        clothe_dict[k] += 1
    # print(clothe_dict)

    answer = 1
    for v in clothe_dict.values():
        answer *= (v+1)

    return answer - 1

# 5
print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
# 3
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
