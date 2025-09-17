'''
p.605 66. 롤케이크 자르기

https://school.programmers.co.kr/learn/courses/30/lessons/132265
소요시간: 27m 37s
'''

def solution(topping):
    answer = 0
    g1 = topping
    g2 = []
    g1_cnt = len(set(topping))
    g2_cnt = 0

    # 빈도수 계산
    g1_count = {}
    g2_count = {}
    for x in topping:
        if x in g1_count: 
            g1_count[x]+=1
        else: 
            g1_count[x]=1
            g2_count[x]=0
    # print(g1_count)

    while len(g1)>0:
        # 두 그룹으로 자르고
        tmp = g1.pop()
        # 각 종류 카운트 업데이트
        g1_count[tmp] -= 1
        g2_count[tmp] += 1

        if g1_count[tmp]==0:
            g1_cnt -= 1
        if g2_count[tmp]==1:
            g2_cnt += 1
        
        # print(tmp)
        # print(g1_count, g2_count)
        # print(g1_cnt, g2_cnt)
        # print()
        # 같으면 카운트
        if g1_cnt==g2_cnt:
            # print(g1, g2)
            answer += 1
    return answer

# 2
print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
# 0
print(solution([1, 2, 3, 1, 4]))
