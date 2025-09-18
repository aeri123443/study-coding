'''
p.646 72. LIS 길이 계산하기
소요시간: 8m 38s
'''

def solution(nums):
    N = len(nums)
    arr = [0]*N
    arr[0] = 1

    for i in range(1, N):
        # print(i)
        tmp = set([1])
        for j in range(i):
            if nums[i] > nums[j]:
                tmp.add(nums[j])
        arr[i] = max(tmp)
        # print()
            
    return max(arr)
# 5
print(solution([1, 4, 2, 3, 1, 5, 7, 3]))
# 1
print(solution([3, 2, 1]))
