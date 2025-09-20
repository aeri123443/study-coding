'''
p.706 83. 구명보트
https://school.programmers.co.kr/learn/courses/30/lessons/42885
소요시간: 20m 21s
'''

def solution(people, limit):
    people.sort()
    i = 0
    j = len(people)-1

    answer = 0
    while i<j:
        answer += 1
        if people[i] + people[j] <= limit:
            i+=1
            j-=1
        else:
            j-=1
    
    if i==j: return answer+1
    else: return answer

# 3
print(solution([70, 50, 80, 50], 100))

# 3
print(solution([70, 80, 50], 100))

# 4
print(solution([30, 40, 40, 50, 60, 70, 80], 100))

# 4
print(solution([30,40,70,70,80], 100))

# 3
print(solution([30,40,50,60,70], 100))
