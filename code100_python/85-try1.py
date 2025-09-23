'''
p.712 85. 기지국 설치
https://school.programmers.co.kr/learn/courses/30/lessons/12979
소요시간: 21m 39s
'''

def solution(n, stations, w):
    answer = 0
    w_range = 2*w+1

    i = 1
    start, end = 1, -1
    for s in stations:
        # print(s, i)
        a, b = s-w, s+w
        if i >= a:
            # print('i >= a')
            start = i = b+1
        else: 
            end = a
            # print(start, end)
            tmp = end - start
            # print(tmp)
            answer += tmp//w_range
            if tmp%w_range!=0: answer += 1
            # print(answer)
            start = i = b+1
    
        # print(start, end, i)
        # print()
  
    if i <= n:
        tmp = n - i + 1
        # print(tmp)
        answer += tmp//w_range
        if tmp%w_range!=0: answer += 1
        # print(answer)

    return answer


# 0
print(solution(5, [2,3,4], 1))

# 6
print(solution(20, [1, 20], 1))

# 4
print(solution(12, [3, 10], 1))

# 3
print(solution(11, [4, 11], 1))

# 1
print(solution(9, [1,6,8], 1))

# 1
print(solution(9, [1,9], 2))

# 1
print(solution(11, [7, 10], 2))

# 3
print(solution(16, [9], 2))

# 1
print(solution(9, [1,6,8], 1))

# 0일때도 구하기
print(solution(4, [2], 2))

