'''
178870. lv2 연속된 부분 수열의 합
https://school.programmers.co.kr/learn/courses/30/lessons/178870
18m 27s
'''

def solution(sequence, k):
    n = len(sequence)
    i, j = 0, 0
    answer = [-1]

    total = sequence[0]
    while i <= j:

        if total < k:
            j += 1
            if j == n: break
            total += sequence[j]
        elif total > k:
            total -= sequence[i]
            i += 1
        else: # total == k

            # answer의 len과 다르면, 덮어쓰기 (어차피 짧아질 일만 남음)
            # answer의 len과 같으면, 유지 (인덱스 적은 걸 유지)
            if answer[0] != j-i+1:
                answer = [j-i+1, [i,j]]
            # answer.append([j-i+1, (i,j)])

            j += 1
            if j == n: break
            total = total + sequence[j] - sequence[i]
            i += 1

    return answer[1]

print()
print(solution([1, 2, 3, 4, 5], 7))
print([2, 3])

print()
print(solution([1, 1, 1, 2, 3, 4, 5], 5))
print([6, 6])

print()
print(solution([2, 2, 2, 2, 2], 6))
print([0, 2])

# print()
# print(solution())
# print()