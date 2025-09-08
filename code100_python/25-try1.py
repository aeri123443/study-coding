'''
p.278 25. 메뉴 리뉴얼
https://school.programmers.co.kr/learn/courses/30/lessons/72411
소요시간: 32m 57s
'''
from itertools import combinations

def choose_menu(arr, num):
    temp = {}
    # 조합 구하기
    for a in arr:
        if len(a) >= num:
            # review: combinations는 이미 이터레이터라 바로 for문에 쓸 수 있음, list 변환 불필요
            temp_com_list = list(combinations(a, num))
            for temp_com in temp_com_list:
                temp_com = ''.join(temp_com)
                if temp_com in temp:
                    temp[temp_com] += 1
                else:
                    temp[temp_com] = 1

    # 가장 많은 수 구하고
    # 그것과 같은 수의 키가 있는지 찾고 반환
    max_keys = []
    if temp:
        max_value = max(temp.values())
        if max_value >= 2:
            max_keys = [k for k,v in temp.items() if v==max_value]
    return max_keys    

def solution(orders, course):
    # 각 원소 문자열 오름차순, 리스트화
    # review: temp = [sorted(order) for order in orders]로 줄일 수 있음
    order_list = []
    for order in orders:
        temp = sorted(list(order))
        order_list.append(temp)
    
    answer_list = []
    for c in course:
        answer_list.extend(choose_menu(order_list, c))

    # 리턴값 오름차순 정렬
    return sorted(answer_list)

# ["AC", "ACDE", "BCFG", "CDE"]
print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
# ["ACD", "AD", "ADE", "CD", "XYZ"]
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
# ["WX", "XY"]
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
      