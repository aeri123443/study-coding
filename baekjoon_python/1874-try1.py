'''
1874. 스택 수열
https://www.acmicpc.net/problem/1874
'''

N = int(input())
target_arr = [int(input()) for _ in range(N)]

# N = 8
# target_arr = [4, 3, 6, 8, 7, 5, 2, 1] # ++++ -- ++ - ++ -----
# N = 5
# target_arr = [1, 2, 5, 3, 4] # return: NO
default_arr = [i for i in range(N)] 

push_arr = []
pop_arr = []
answer_arr = []

i = 1
is_vaild = True

for target in target_arr:
    if i <= target:
        push_arr.extend([j for j in range(i,target)])
        pop_arr.append(target)
        answer_arr.extend(['+']*(target-i+1))
        i = target+1
    else:
        if len(push_arr)>0 and push_arr[-1]==target:
            pop_arr.append(push_arr.pop())
        else:
            print('NO')
            is_vaild = False
            break
    answer_arr.append('-')
    # print('push_arr', push_arr)
    # print('pop_arr', pop_arr)
    # print('answer_arr', answer_arr)
    # print()

if is_vaild and len(pop_arr)==N:
    print(*answer_arr, sep='\n')

