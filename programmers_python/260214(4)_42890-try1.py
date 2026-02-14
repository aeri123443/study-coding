'''
42890. Lv. 2 후보키
https://school.programmers.co.kr/learn/courses/30/lessons/42890
49m 31s
'''
from itertools import combinations

def solution(relation):
    answer = set()
    n = len(relation[0])
    idx_arr = [i for i in range(n)]
    
    for l in range(1, n+1):

        # 어차피 남은 배열로 이후의 길이를 만들 수 없으니 빠져나감
        # if l > len(idx_arr):
        #     break

        for per in combinations(idx_arr, l):

            for s in answer:
                if not set(s)-set(per):
                    break
                
            else:
                
                tmp_set = set()
                for row in relation:
                    tmp_string = '|'.join([row[i] for i in per])
                    if tmp_string in tmp_set:
                        break
                    tmp_set.add(tmp_string)
                else:
                    # answer.add(set(per))

                    answer.add(tuple(per))
                    # print(len(per)list(per))
                    # for i in per:
                    #     if i in not_selected: not_selected.remove(i)
                
    return len(answer)   

print()
print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
print(2)

# print()
# print(solution())
# print()
