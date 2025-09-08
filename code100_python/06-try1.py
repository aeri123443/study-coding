'''
p.125 06. 실패율
https://school.programmers.co.kr/learn/courses/30/lessons/42889
소요시간: 36m 54s
'''

# 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

def solution(N, stages):
    # 단계-실패 횟수 딕셔너리 
    dict_cnt = {}
    dict_answer = {}
    for i in range(N+1):
        dict_cnt[i+1]=0

    # 실패율 계산
    for item in stages:
        dict_cnt[item] += 1
    # print(dict_cnt)

    member = len(stages)
    for i in range(N):           
        stage = i+1
        if member==0:
            dict_answer[stage] = 0
        else:
            dict_answer[stage] = dict_cnt[stage] / member
            member -= dict_cnt[stage]
    # print(dict_answer)

    # 실패율 정렬
    answer = sorted(dict_answer.items(), key=lambda x:x[1], reverse=True)
    answer = [ x[0] for x in answer]
    return answer

# [3,4,2,1,5]
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3])) 
# [4,1,2,3]
print(solution(4, [4,4,4,4,4]))
# [1,2,3,4]
print(solution(4, [1,1,1,1,1]))
# [4,2,1,3,5,6] 
print(solution(6, [4,4,2,4,2,2]))
