'''
43238. Lv.3 입국심사
https://school.programmers.co.kr/learn/courses/30/lessons/43238
56m 26s
'''

def solution(n, times):
    left = 1
    right = min(times)*n

    while left+1 < right:
        mid = (left + right)//2
        mid_n = sum([mid//x for x in times])
        # print(left, right, mid, mid_n)

        if mid_n < n:
            left = mid
        else:
            right = mid

    return right

print()
print(solution(6, [7, 10]))
print(28)
