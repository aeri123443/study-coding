'''
42747. lv2 H-Index
https://school.programmers.co.kr/learn/courses/30/lessons/42747
다시 풀기
'''

def solution(citations):
    n = len(citations)
    h_arr = [ n-i for i in range(n)]
    citations.sort()

    # print(citations)
    # print(h_arr)

    idx = 0
    for i in range(n):
        if citations[i] <= h_arr[i]:
            idx = i
            # return citations[i-1]

    # print()
    # print(idx, citations[idx],h_arr[idx] )
    # print(citations)
    # print(h_arr)
    if citations[idx] == h_arr[idx]: return h_arr[idx]
    else: 
        if idx < n-1:
            return h_arr[idx+1]
        else:
            return h_arr[-1]
    # return answer

# 3
print(solution([3, 0, 6, 1, 5]))

# 3
print(solution([5,3,4,1,2,0]))

# 4
print(solution([8,1,10,9,4]))

# 5
print(solution([8,1,10,9,4, 11, 12]))

# 1000??
print(solution([1000]*1000))

# 999
print(solution([10000]*1000))

#1
print(solution([1]))
print(solution([2]))
print(solution([0]))

#1
print(solution([0, 0, 0, 100]))
#2
print(solution([100, 100]))