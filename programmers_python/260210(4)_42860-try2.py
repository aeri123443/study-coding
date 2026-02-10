'''
42860. Lv.2 조이스틱
https://school.programmers.co.kr/learn/courses/30/lessons/42860
'''

def solution(name):
    # print(name)
    N = len(name)

    ud_cnt = sum( [ min(ord(x)-65, 91-ord(x)) for x in name ] )
    # print(ud_cnt)

    lr_cnt = N-1 # 쭉 직진
    i = 0
    for j in range(N):
        if name[j] == 'A':
            continue

        if i!=j:
            path1 = 2*i + N-j
            path2 = 2*(N-j) + i
            lr_cnt = min(lr_cnt, path1, path2)
        
        i = j

    # 끝부분 처리
    # A 무리가 끝에 있다는 뜻이므로, 그냥 오른쪽으로 쭉 가는게 빠름
    if i != N-1:
        lr_cnt = min(lr_cnt, i)

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