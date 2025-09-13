'''
p.506 51. 양궁대회  
https://school.programmers.co.kr/learn/courses/30/lessons/92342
조합으로 풀어어보기
'''

from itertools import combinations_with_replacement

def solution(n, info):
    apeach_list = [*info]
    apeach_list.reverse()
    score_combi = list(combinations_with_replacement([i for i in range(11)], n))

    max_minus = 0
    answer_list = []
    
    for s_list in score_combi:
        lion_list = [0]*11
        for s in s_list: 
            lion_list[s]+=1

        apeach_score, lion_score = 0, 0   
        for i in range(11):
            if lion_list[i]==apeach_list[i]==0:
                continue
            if lion_list[i]>apeach_list[i]:
                lion_score += i
            else: 
                apeach_score += i
        if lion_score > apeach_score:   
            if lion_score-apeach_score==max_minus:
                for j in range(11):
                    if lion_list[j] > answer_list[j]:
                        answer_list = lion_list
                        break
                    elif lion_list[j] < answer_list[j]:
                        break
            elif lion_score-apeach_score>max_minus:
                max_minus = lion_score-apeach_score
                answer_list = lion_list

        
    if max_minus==0: return [-1]
    answer_list.reverse()
    return answer_list
    
# [0,2,2,0,1,0,0,0,0,0,0]
print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
# [-1]
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
# [1,1,2,0,1,2,2,0,0,0,0]
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
# [1,1,1,1,1,1,1,1,0,0,2]
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))
