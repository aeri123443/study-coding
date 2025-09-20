'''
p.701 81. 부분 배낭 문제
소요시간: 12m 52s
'''

def solution(items, weight_limit):

    for i, [w,v] in enumerate(items):
        items[i].append(v/w)
    items.sort(key=lambda x:x[2], reverse=True)
    
    answer = 0
    remain_weight = weight_limit
    for w, v, x in items:
        if w <= remain_weight:
            answer += v
            remain_weight -= w
        else:
            answer += x * (remain_weight)
            return round(answer, 2)
    
# 27.33
print(solution([[10, 19], [7, 10], [6, 10]], 15))

# 240
print(solution([[10, 60], [20, 100], [30, 120]], 50))
