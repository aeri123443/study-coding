'''
389480. LV2. 완전범죄
https://school.programmers.co.kr/learn/courses/30/lessons/389480
'''

def solution(info, n, m):
    info.sort(key=lambda x: x[1], reverse=True)
    answer = 0

    for i, j in info:
        print(i, j)
        print(m)
        if m - j < 0:
            break
        m -= j
        answer += 1

    a_sum = sum(x[0] for x in info[answer:])
    print(info[answer:])
    if a_sum <= n:
        return a_sum
    else:
        return -1

# 2
print(solution([[1, 2], [2, 3], [2, 1]], 4, 4))
# 0
# print(solution([[1, 2], [2, 3], [2, 1]], 1, 7))
# # 6
# print(solution([[3, 3], [3, 3]], 7, 1))
# # -1
# print(solution([[3, 3], [3, 3]], 6, 1))
