'''
p.704 82. 예산
https://school.programmers.co.kr/learn/courses/30/lessons/12982
소요시간: 7m 36s
'''

def solution(d, budget):
    d.sort()
    for i, x in enumerate(d):
        if budget >= x:
            budget -= x
        else:
            return i
        
    return len(d)

# 3
print(solution([1,3,2,5,4], 9))

# 4
print(solution([2,2,3,3], 10))
