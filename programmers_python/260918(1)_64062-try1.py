'''
64062. 2019 카카오 개발자 겨울 인턴십 - 징검다리 건너기
https://school.programmers.co.kr/learn/courses/30/lessons/64062

문제 분석: 27m 30s
코드 작성: 46m 59s

시간 초과 -> 단조 덱으로 변경
'''

# 최하단 노드의 첫번째 인덱스를 구함
def cal_b(n):
    # n보다 크고 가장 가까운 2의 배수
    b = 1
    while b < n:
        b *= 2

    return b

# 최대값 세그먼트 트리
def make_max_tree(stones, b):
    tree = [0] * (b*2+1)

    for i, v in enumerate(stones):
        tid = i + b
        tree[tid] = v

    depth = b
    while depth > 1:
        for tid in range(depth, depth*2, 2):
            tree[tid//2] = max(tree[tid], tree[tid+1])

        depth //= 2

    return tree

# sl~sr 최대값 반환
def get_seg_max(max_tree, sl, sr):
    li = sl
    lv = max_tree[sl]
    ri = sr
    rv = max_tree[sr]

    while li <= ri:
        if max_tree[li] > lv: lv = max_tree[li]
        if max_tree[ri] > rv: rv = max_tree[ri]

        li = (li + 1) // 2
        ri = (ri - 1) // 2

    return lv if lv > rv else rv

def solution(stones, k):
    # 세그먼트 트리
    n = len(stones)
    if n==k: return min(stones) # 여기서 n==1인 경우 걸러짐

    b = cal_b(n)
    max_tree = make_max_tree(stones, b)

    # 구간을 슬라이딩하며 최댓값을 업데이트
    sl = b
    sr = b + k - 1
    answer = float('inf') # 구간 최대값의 최소값


    while sr < b+n:
        seg_max = get_seg_max(max_tree, sl, sr)
        if seg_max < answer: answer = seg_max

        sl += 1
        sr += 1

    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)) #3
print(solution([4,9,7,5,3,5,6,8,4,2,7,9], 5)) #7
