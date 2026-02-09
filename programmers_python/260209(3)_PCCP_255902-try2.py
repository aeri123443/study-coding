
'''
Lv. 2 [PCCP 모의고사 #1] 3번 - 유전법칙
https://school.programmers.co.kr/learn/courses/20847/lessons/255902
try1까지 total 1h 02m 18s
시간복잡도 미리 계산하고 들어가기
'''

'''
각 완두콩은 자가 수분해서 정확히 4개의 완두콩 후손을 남긴다.
잡종 완두콩(Rr)은 자가 수분해서 첫째는 RR, 둘째와 셋째는 Rr, 넷째는 rr 형질의 후손을 남긴다.
순종 완두콩(RR, rr)은 자가 수분해서 자신과 같은 형질의 후손을 남긴다.

완두콩의 세대와 해당 세대에서 몇 번째 개체인지를 알면 형질을 바로 계산하는 프로그램을 만들려 합니다.
'''

def solution(queries):
    childs = {
        'RR': ['RR', 'RR', 'RR', 'RR'],
        'rr': ['rr', 'rr', 'rr', 'rr'],
        'Rr': ['RR', 'Rr', 'Rr', 'rr']
    }

    # 경로 찾기
    path = []
    def find_path(n, p):
        nonlocal path

        if n==1:
            path.append([1,1])
            return
        
        path.append([n, p])
        find_path(n-1, ( (p-1)//4 + 1 ))

    def find_type(path):
        stack = path

        # 첫번째는 무조건 Rr
        stack.pop()
        now = 'Rr'
        while stack:
            n, p = stack.pop()
            # print(n, p, now, (p-1)%4)
            now = childs[now][(p-1)%4]
            # print(now)
        return now
    
    # 경로를 타고가면서 정답 출력
    answer = []
    for n, p in queries:
        path = []
        find_path(n, p)
        # print(path)
        answer.append( find_type(path) )

    return answer

print()
print(solution([[3, 5]]))
print(["RR"])

print()
print(solution([[3, 8], [2, 2]]))
print(["rr", "Rr"])

print()
print(solution([[3, 1], [2, 3], [3, 9]]))
print(["RR", "Rr", "RR"])

print()
print(solution([[4, 26]]))
print(["Rr"])

print()
print(solution([[16, 1073741824]]))
print(["rr"])

# print(4**15) # 1073741824
