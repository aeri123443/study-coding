'''
12891. <실버 2> DNA 비밀번호
https://www.acmicpc.net/problem/12891
'''

from pprint import pprint
import sys
from collections import Counter

input = sys.stdin.readline

guide_set = {}
guide_list = ['A', 'C', 'G', 'T']
c_counter = {}

S, P = map(abs, map(int, input().split()))
str_arr = list(input().strip())
# print(str_arr)

def is_correct():
    for k, v in guide_set.items():
        if c_counter[k] < v: 
            return False
    return True

# 'A', 'C', 'G', 'T'에 대한 최소 문자 수
tmp_arr = list(map(int, input().split()))
for i in range(4):
    guide_set[guide_list[i]] = tmp_arr[i]
# pprint(guide_set)


# 초기 카운터
c_counter = Counter( str_arr[0:P] )
# pprint(str_arr[0:P])
# pprint(c_counter)
answer = 0

if is_correct(): answer+=1

# print(answer)

# 슬라이딩 윈도우
s_idx = 0
e_idx = P-1
while e_idx < S-1:
    # 카운터 넣고 빼고
    char_remove = str_arr[s_idx] # 제거될 문자
    char_add = str_arr[e_idx+1] # 추가될 문자
    # print('char_remove, char_add : ', char_remove, char_add)
    c_counter[char_remove] -= 1
    c_counter[char_add] += 1
    # pprint(c_counter)
    if is_correct(): answer+=1

    s_idx+=1
    e_idx+=1

print(answer)
