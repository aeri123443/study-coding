'''
42884. Lv.3 단속카메라
https://school.programmers.co.kr/learn/courses/30/lessons/42884
'''
def solution(routes):
    cams = []
    routes.sort(key=lambda x:x[1])

    for a, b in routes:
        if not cams:
            cams.append(b)
            continue
        
        is_captured = False
        for x in cams:
            if a <= x <= b:
                is_captured = True
                break
        if not is_captured:
            cams.append(b)

    # print(routes)
    return len(cams)

print()
print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))
print(2)

print()
print(solution([[1,5], [2,6], [3,7]]))
print(1)

# print()
# print(solution())
# print()

# print()
# print(solution())
# print()
