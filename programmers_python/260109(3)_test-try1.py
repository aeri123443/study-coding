'''
p.180 14. 표 편집
https://school.programmers.co.kr/learn/courses/30/lessons/81303
소요시간: 97m 14s
'''

def solution(participant, completion):
    participant.sort()
    completion.sort()
    # print(participant)
    # print(completion)

    n = len(participant)
    for i in range(n):
        if i == n-1:
            return participant[i]
        if participant[i] != completion[i]:
            return participant[i]

# "leo"
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
      
# "vinko"
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))

# "mislav"
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
      