'''
340212. Lv.2 [PCCP 기출문제] 2번 / 퍼즐 게임 챌린지
https://school.programmers.co.kr/learn/courses/30/lessons/340212
41m 53s
'''

def solution(diffs, times, limit):
   
    N = len(diffs)
    
    def solved(level):
        time_append = 0
        total_time = 0
        for i in range(N):
            diff, time_cur = diffs[i], times[i]
            if diff <= level: 
                total_time += time_cur                
            else:
                total_time += ( (diff-level) * (times[i-1]+time_cur) + time_cur )

            # if i<10 and level<5: print(level, i, time_prev, total_time)
            if total_time > limit:
                return -1
        return total_time
    
    left, right = 1, max(diffs)+1
    while left < right:
        lv = (left+right)//2
    # for lv in range(1, max(diffs)+1):
        result = solved(lv)
        if result > 0:
            right = lv
        else:
            left = lv+1
    
    return right
