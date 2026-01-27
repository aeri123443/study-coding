'''
42578. lv2 의상
https://school.programmers.co.kr/learn/courses/30/lessons/42578
'''


def solution(clothes):
    hash_map = {}

    for _, x in clothes:
        if x not in hash_map:
            hash_map[x] = 0
        hash_map[x] += 1
    # print(hash_map)
    
    answer = 1
    for v in hash_map.values():
        answer *= (v+1)

    return answer-1

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