'''
67258. Lv.3 보석 쇼핑
https://school.programmers.co.kr/learn/courses/30/lessons/67258
60m
'''

def solution(gems):
    N = len(gems)
    counter = {x:0 for x in gems}
    max_set = len(counter)
    gems = [0] + gems
    # print(counter)

    i = j = 1
    answer = [N, 1, N] # 구간 길이, 시작보석, 끝보석
    counter[gems[j]] = 1
    cur_set = 1
    while i<=j:
        # print(i,j)
        
        # print(i, j, cur_set, counter)
        if cur_set < max_set:
            j+=1
            if j > N: break
            if counter[ gems[j] ]==0:
                cur_set += 1
            counter[ gems[j] ] += 1
        elif cur_set == max_set:
            
            # answer 업데이트
            if j-i+1 < answer[0]:
                answer = [j-i+1, i, j]
            # print('ok', i,j, answer)
            # print(counter)
            # print(i,j)
            # print(gems[i])
            # print(counter[ gems[i] ])
            counter[ gems[i] ] -= 1
            if counter[ gems[i] ] == 0:
                cur_set -= 1
            i+=1

    return answer[1:]

print()
print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print([3, 7])

print()
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print([1, 3])

print()
print(solution(["XYZ", "XYZ", "XYZ"]))
print([1, 1])

print()
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
print([1, 5])

print()
print(solution(["A", "B", "D", "A", "D", "A", "A", "A", "B", "C", "D"]))
print([8,11])

print()
print(solution(["A", "B", "C", "D", "A", "A", "A", "B", "C", "D"]))
print([1,4])

# print()
# print(solution())
# print()