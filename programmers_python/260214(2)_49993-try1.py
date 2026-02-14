'''
49993. Lv. 2 스킬트리
https://school.programmers.co.kr/learn/courses/30/lessons/49993
7m 40s
'''

def solution(skill, skill_trees):
    answer = 0
    first = set(skill)

    for s in skill_trees:
        p = 0
        can_learn = True
        for c in s:
            if c in first:
                if c == skill[p]:
                    p += 1
                else:
                    # print('not', s)
                    can_learn = False
                    break
        if can_learn:
            # print('can', s)
            answer += 1

    return answer

print()
print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
print(2)

# print()
# print(solution())
# print()