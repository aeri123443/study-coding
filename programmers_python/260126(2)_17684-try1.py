'''
17684. [3차] 압축
https://school.programmers.co.kr/learn/courses/30/lessons/17684
'''
def solution(msg):
    N = len(msg)
    cnt = 26
    answer = []
    hash_map = {chr(65+i): i+1 for i in range(cnt)}
    # print(hash_map)

    i = 0
    while i<N:
        s_word = msg[i]
        j = i+1
        while j<N:
            if s_word+msg[j] in hash_map:
                s_word += msg[j]
                j+=1
            else:
                break
        # print(s_word, i, j, hash_map[s_word])
        answer.append(hash_map[s_word])
        cnt+=1
        i = j
        if j<N:
            hash_map[s_word+msg[j]] = cnt
                # print(hash_map)
        else:
            break
        
    return answer

print()
print(solution('KAKAO'))
print([11, 1, 27, 15])

print()
print(solution('TOBEORNOTTOBEORTOBEORNOT'))
print([20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34])

print()
print(solution('ABABABABABABABAB'))
print([1, 2, 27, 29, 28, 31, 30])

# 최대최소케이스
# 경곗값케이스
# 시간초과 확인