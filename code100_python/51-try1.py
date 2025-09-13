'''
p.506 51. 양궁대회  
https://school.programmers.co.kr/learn/courses/30/lessons/92342
소요시간: 115m 52s
'''

def dfs(minus):
    global win_map, group_cnt, max_num, answer, apeach_win, lion_win
    for cnt in group_cnt:        
        if minus-cnt==0 and len(win_map[cnt])>0:
            pop_point = win_map[cnt].pop()
            # print(pop_point, lion_win)
            if cnt!=1: apeach_win.remove(pop_point)
            lion_win.add(pop_point)
            if sum(lion_win) > sum(apeach_win):
                # print("win", sum(lion_win) - sum(apeach_win), lion_win)
                if max_num == sum(lion_win) - sum(apeach_win):
                    if min(answer) > min(lion_win):
                        answer = sorted(lion_win)
                        max_num = sum(lion_win) - sum(apeach_win)
                elif max_num < sum(lion_win) - sum(apeach_win):
                    answer = sorted(lion_win)
                    max_num = sum(lion_win) - sum(apeach_win)     
            if cnt!=1: apeach_win.add(pop_point)
            lion_win.remove(pop_point)
            win_map[cnt].append(pop_point)
            return

        if minus-cnt>0:
            if len(win_map[cnt])>0:
                pop_point = win_map[cnt].pop()
                if cnt!=1: apeach_win.remove(pop_point)
                lion_win.add(pop_point)
                dfs(minus-cnt)
                if cnt!=1: apeach_win.add(pop_point)
                lion_win.remove(pop_point)
                win_map[cnt].append(pop_point)
        else:
            if len(win_map[cnt])>0:
                # pop_point = win_map[cnt].pop()
                # if cnt!=1: apeach_win.remove(pop_point)
                # lion_win.add(pop_point)
                if sum(lion_win) > sum(apeach_win):
                    # print("win", sum(lion_win) - sum(apeach_win), lion_win)
                    if max_num == sum(lion_win) - sum(apeach_win):
                        if min(answer) > min(lion_win):
                            answer = sorted(lion_win)
                            max_num = sum(lion_win) - sum(apeach_win)
                    elif max_num < sum(lion_win) - sum(apeach_win):
                        answer = sorted(lion_win)
                        max_num = sum(lion_win) - sum(apeach_win)     
                # if cnt!=1: apeach_win.add(pop_point)
                # lion_win.remove(pop_point)
                # win_map[cnt].append(pop_point)

def solution(n, info):
    global win_map, group_cnt, max_num, answer, apeach_win, lion_win
    # 라이언의 과녁 수 정렬
    win_map = {}
    group_cnt = []
    max_num = 0
    answer = [float('inf')]
    apeach_win = set()
    lion_win = set()

    info.reverse()

    for i, v in enumerate(info):
        if not v+1 in win_map:
            group_cnt.append(v+1)
            win_map[v+1] = [i]
        else:
            win_map[v+1].append(i)
        if v>0: apeach_win.add(i)
    # print('win_map', win_map)
    # print('group_cnt', group_cnt)
    # print('apeach_win', apeach_win)

    dfs(n)
    group_cnt.reverse()
    dfs(n)
    last_answer = [0]*11

    if max_num == 0:
        return [-1]
    else:
        # print(answer)
        for i in answer: last_answer[i]=info[i]+1
        if sum(last_answer) < n: last_answer[0] = n-sum(last_answer)
    last_answer.reverse()    
    return last_answer


# [0,2,2,0,1,0,0,0,0,0,0]
print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
# [-1]
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
# [1,1,2,0,1,2,2,0,0,0,0]
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
# [1,1,1,1,1,1,1,1,0,0,2]
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))

