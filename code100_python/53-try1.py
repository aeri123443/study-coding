'''
p.520 53. 사라지는 발판  
https://school.programmers.co.kr/learn/courses/30/lessons/92345
실력 오르면 다시 풀어보기.. 풀지도 못하고 이해도 못하겠고
'''
from itertools import permutations

def solution(n, weak, dist):
    for i in range(len(weak)):
        weak.append(weak[i]+n)
    # print(weak)

    perm_members = list(permutations(dist, len(dist)))
    # print(list(perm_members))

    answer = float('inf')
    for i in range(len(weak)//2):
        for members in perm_members:
            members = list(members)
            # 투입 멤버 수
            cnt = 1
            # 최근 투입된 멤버가 이동 가능한 횟수
            remain_move = members[cnt-1]
            # 다음으로 넘어갈 수 있을지 확인
            for j in range(i+1, i+(len(weak)//2)):
                # print(weak[j]-weak[j-1], remain_move)
                if weak[j]-weak[j-1] <= remain_move:
                    # print(members[cnt-1], 'can go', j)
                    remain_move -= weak[j]-weak[j-1]
                else:
                    # print(members[cnt-1], 'cannot go', j)
                    if cnt >= len(dist): 
                        if j < i+(len(weak)//2):
                            cnt = answer
                        break   
                    cnt += 1
                    remain_move = members[cnt-1]
            # print(i, members, cnt)
            # print()
            answer = min(answer, cnt)
    if answer == float('inf'):
        return -1
    return answer

# 2
print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
# 1
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
# -1 테케 추가
# print(solution(12, [1, 3, 4, 9, 10], [1, 1, 1]))
print(solution(12, [1, 3, 5, 9, 10], [1, 1, 1]))
# 5
print(solution(12, [1, 3, 5, 9, 11], [1, 1, 1, 1, 1]))
