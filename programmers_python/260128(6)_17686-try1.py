'''
17686. lv2 [3차] 파일명 정렬
https://school.programmers.co.kr/learn/courses/30/lessons/17686
39m 37s
'''

import re
from pprint import pprint
def solution(files):
    N = len(files)
    # [f_name, idx, head, number]
    file_list = []

    # 전처리
    for i in range(N):
        f_name = files[i]
        re_result = re.match(r'([^0-9]+)([0-9]{0,5})', f_name)
        head, num = re_result.group(1), re_result.group(2)
        # print(head, num)
        file_list.append([f_name, i, head.lower(), int(num)])
    # pprint(file_list)

    # 정렬
    file_list.sort(key=lambda x: (x[2], x[3], x[1]))
    # pprint(file_list)

    # answer = sorted(mapping.items)
    return [x[0] for x in file_list]

print()
print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"])

print()
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
print(["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"])

# print()
# print(solution())
# print()

# print()
# print(solution())
# print()