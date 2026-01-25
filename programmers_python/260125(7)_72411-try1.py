'''
72411. lv2 메뉴 리뉴얼
https://school.programmers.co.kr/learn/courses/30/lessons/72411
'''

# 각 손님들이 주문할 때 --가장 많이 함께 주문한 단품메뉴들--을 코스요리 메뉴로 구성
# 코스요리 메뉴는 최소 2가지 이상의 단품메뉴
# 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만..

# 정답은 각 코스요리 메뉴의 구성을 문자열 형식으로 배열에 담아 사전 순으로 오름차순 정렬
# 배열의 각 원소에 저장된 문자열 또한 알파벳 오름차순으로 정렬되어야 합니다.
#  가장 많이 함께 주문된 메뉴 구성이 여러 개라면, 모두 배열에 담아 return

import sys
from pprint import pprint 
input = sys.stdin.readline
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer_list = []
    for iter_num in course:

        # iter_num에 대한 모든 조합을 돌리고 모으기
        tmp = []
        for order in orders:

            # iter_num보다 order가 적으면 패스
            if iter_num > len(order): continue

            # print(order)
            # 오름차순 정렬
            order = sorted(list(order))
            # print(order)
            com = list(combinations(order, iter_num))
            # print(com)
            for x in com:
                tmp.append(''.join(x))
            # print(tmp)
        
        # 조합이 없으면 pass
        if not tmp:
            continue
        
        # 조합에 대해 cnt
        tmp_counter = Counter(tmp)
        # print(tmp_counter)
        # 조합 수가 가장 큰 것은?
        max_num = max(tmp_counter.values())
        # max_num이 2보다 작으면 패스
        if max_num<2: continue
        # 해당 조합 반환
        for k,v in tmp_counter.items():
            if v==max_num:
                answer_list.append(k)
    
    return sorted(answer_list)


print()
print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(["AC", "ACDE", "BCFG", "CDE"])

print()
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(["ACD", "AD", "ADE", "CD", "XYZ"])

print()
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
print(["WX", "XY"])