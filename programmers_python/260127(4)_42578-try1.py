'''
42578. lv2 의상
https://school.programmers.co.kr/learn/courses/30/lessons/42578
시간초과
'''

from itertools import combinations

def solution(clothes):
    hash_map = {}

    for a, b in clothes:
        if b not in hash_map:
            hash_map[b] = 0
        hash_map[b] += 1
    # print(hash_map)
    
    # 옷 종류에 대해서만 조합을 돌림
    combi = []
    for i in range(len(hash_map)):
        combi.extend( list(combinations(hash_map.keys(), i+1)) )
        # print(hash_map.keys())
        # print(i)
    # print(combi)

    answer = 0
    for x in combi:
        tmp = 1
        for y in x:
            tmp *= hash_map[y]
            # print(y)
        # print(tmp)
        answer += tmp
    # answer = 0
    return answer

print()
print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(5)


print()
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
print(3)

# 종류 높여서 가보자
# 최대최소도 체크
# print()
# print(solution())
# print()