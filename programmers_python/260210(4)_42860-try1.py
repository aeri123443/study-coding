'''
42860. Lv.2 조이스틱
https://school.programmers.co.kr/learn/courses/30/lessons/42860
'''

def solution(name):
    N = len(name)

    # 상하 버튼은 누적변수로 관리
    # 좌우 이동용 배열 생성(A기준 경로 압축: A없으면 (), 있으면 연속된 A의 (i,j))
    ud_cnt = 0
    lr_list = []
    a_cnt = 0 # 연속된 A 개수 확인

    for i, x in enumerate(name):
        if x=='A': 
            a_cnt += 1
        else:
            if a_cnt > 0:
                lr_list.append((i-a_cnt, i))
                a_cnt = 0
            num = ord(x)
            ud_cnt += min(num-65, 91-num)
            lr_list.append(())
    if a_cnt > 0:
        lr_list.append((N-a_cnt, N))

    # print(ud_cnt, lr_list)

    if len(lr_list)==1 and lr_list[0]:
        return 0
    
    # 좌우 경로 확인
    lr_cnt = N-1
    for tu in lr_list:
        if tu: # A가 한개 이상 있다는 의미!
            i, j = tu

            # 오른쪽으로 갔다가 왼쪽으로 돌아갈 때의 좌우 조작 횟수
            tmp_right = 2*(i-1) + (N-j)
            if tmp_right >= 0:  lr_cnt = min(lr_cnt, tmp_right)

            # 왼쪽으로 갔다가 오른쪽으로 돌아갈 때의 좌우 조작 횟수
            tmp_left = (i) + 2*(N-j)-1
            if tmp_left >= 0:  lr_cnt = min(lr_cnt, tmp_left)

            # print(tu , lr_cnt, tmp_right, tmp_left)
            # lr_cnt = min(lr_cnt, tmp_right, tmp_left)
    # print(lr_cnt)

    return ud_cnt + lr_cnt

print()
print(solution("JAZ"))
print(11)

print()
print(solution("JEROEN"))
print(56)

print()
print(solution("ZAZAAAAAAAB"))
print(7)

print()
print(solution("ABZAAA"))
print(4)

print()
print(solution("A"))
print(0)

print()
print(solution("AAA"))
print(0)

print()
print(solution("B"))
print(1)

print()
print(solution("AB"))
print(2)

print()
print(solution("BA"))
print(1)

# print()
# print(solution())
# print()