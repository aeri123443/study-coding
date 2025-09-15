'''
p.568 57. 문자열 내 마음대로 정렬하기 
https://school.programmers.co.kr/learn/courses/30/lessons/12933
소요시간: 9m 34s
'''

def solution(n):
    arr = []

    tmp=n
    while tmp>=10:
        arr.append(tmp%10)
        tmp = tmp//10
    arr.append(tmp)

    arr.sort()

    answer = 0
    # ten = 0
    for i in range(len(arr)):
        answer += arr[i]*(10**i)
    return answer

# 873211
print(solution(118372))
# 8731100
print(solution(1180370))