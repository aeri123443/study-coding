'''
12946. lv2 하노이의 탑
https://school.programmers.co.kr/learn/courses/30/lessons/12946
14m 38s
'''


def solution(n):
    answer = []

    # from에 있는 것을 via를 통해 to에 num개 옮겨라
    def hanoi(n, f, v, t): # num, from, via, to
        nonlocal answer

        if n==1:
            answer.append([f,t])
            return
        
        # from -> via n-1개 옮기기
        hanoi(n-1, f, t, v)
        # 가장 큰 원판을 from->to
        answer.append([f,t])
        # via에 옮겼던 것을 to로 (n-1개)
        hanoi(n-1, v, f, t)

    hanoi(n, 1, 2, 3)
    
    return answer

print()
print(solution(2))
print([ [1,2], [1,3], [2,3] ])

print()
print(solution(3))
print()
