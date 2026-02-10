'''
340199. Lv.1 [PCCE 기출문제] 9번 / 지폐 접기
https://school.programmers.co.kr/learn/courses/30/lessons/340199
'''

def solution(wallet, bill):

    answer = 0

    while min(bill) > min(wallet) or max(bill) > max(wallet):
        if bill[0] > bill[1]:
            bill[0] = bill[0] // 2
        else:
            bill[1] = bill[1] // 2

        answer += 1

    return answer

print(solution([30, 15], [26, 17]))
print(solution([50, 50], [100, 241]))