'''
p.497 49. 피로도
https://school.programmers.co.kr/learn/courses/30/lessons/87946
소요시간: 84m 53s
순열도 겸사겸사 공부해보고 싶었음...
'''
def backtrack(arr, hp, max_num):
    global answer_max
    # print(arr, hp, max_num)

    if len(arr)==0:
        return [True, max_num]

    for i, [need,dem] in enumerate(arr):
        remain_dem = hp - dem
        if hp >= need and remain_dem>=0:
            remain = arr[:i] + arr[i+1:]
            recall = backtrack(remain, remain_dem, max_num+1)
            if recall[0] == True:
                answer_max = recall[1]
                return recall
            
    answer_max = max (answer_max, max_num)
    return [False, max_num]

def solution(k, dungeons):
    global answer_max
    answer_max = 0
    backtrack(dungeons, k, 0)

    return answer_max

# 3
print(solution(80, [[80,20],[50,40],[30,10]]))
print(solution(100, [[100, 20], [60, 30], [50, 20], [10, 20]]))
print(solution(100, [[100, 20], [60, 30], [50, 20], [40, 20]]))
print(solution(100, [[100, 20], [60, 30], [50, 20], [10, 40]]))

