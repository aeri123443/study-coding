'''
p.709 84. 귤 고르기
https://school.programmers.co.kr/learn/courses/30/lessons/138476
소요시간: 21m 39s
'''

from collections import Counter

def solution(k, tangerine):
    # counter -> 빈도순 정렬
    # review: sorted(cnt.values(), reverse = True)로 하면 알아서 리스트로 반환됨
    cnt = sorted([[k,v] for k,v in Counter(tangerine).items()], key=lambda x:x[1], reverse=True)
    # print(cnt)

    # 정답 구하기
    answer = 0
    for _,v in cnt:
        # print(k, v)
        k -= v
        answer += 1
        if k <= 0:
            break
        
    return answer

# 1
print(solution(1, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(1, [5]))

# 4
print(solution(7, [1,2,2,3,3,3,4,5,6]))
# 2
print(solution(7, [1,2,2,2,2,4,4,4,4,3,5,6]))


# 3
print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))

# 2
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))

# 1
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))
