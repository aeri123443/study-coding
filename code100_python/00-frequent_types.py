'''
리스트: 투 포인터
- 정렬된 배열에서 두 수의 합이 특정 값이 되는 쌍을 찾는 문제
- 배열의 양 끝에서 시작하는 두 포인터를 이동시켜 합을 찾음
'''

def two_sum(nums, target):
    nums.sort()
    left, right = 0, len(nums)-1
    while left < right:
        current_num = nums[left] + nums[right]
        if current_num == target:
            return [nums[left], nums[right]]
        elif current_num < target:
            left += 1
        else:
            right -= 1
    return []

# print(two_sum([2, 7, 15, 11], 9))  # [2, 7]

'''
리스트: 슬라이딩 윈도우로 최대 부분 합 찾기
- 고정된 크기의 윈도우를 이동시키며 배열의 최대 부분합을 구하는 문제
- 윈도우 크기를 유지하면서 합을 계산해 최대값을 찾음
'''

def max_subarray_sum(arr, k):
    max_sum = sum(arr[:k])
    current_sum = max_sum
    
    for i in range(k, len(arr)):
        current_sum = current_sum + arr[i] - arr[i-k]
        max_sum = max(max_sum, current_sum)
    
    return max_sum
# print(max_subarray_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))  # 24


'''
리스트: 이진 탐색 정렬된 배열에서 특정 값을 효율적으로 찾는 문제
- bisect 모듈을 이용해 이진 탐색으로 값의 위치를 찾음
'''

import bisect

def binary_search(arr, target):
    index = bisect.bisect_left(arr, target)
    if index < len(arr) and arr[index]==target:
        return index
    else:
        return -1
    
# print(binary_search([1, 2, 3, 4, 5], 3))  # 2
# print(binary_search([1, 2, 3, 4, 5], 6))  # -1

'''
스택: 괄호 검사
- 주어진 문자열에서 괄호들이 올바르게 쌍을 이루고 있는지 확인하는 문제
- 스택을 이용해 여는 괄호를 저장하고, 닫는 괄호가 나올 때 쌍을 맞춤
'''

def is_valid_parentheses(s):
    stack = []
    mapping = {')':'(', '}':'{', ']':'['}
    
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

# print(is_valid_parentheses("()[]{}"))  # True
# print(is_valid_parentheses("[{()}]"))  # True
# print(is_valid_parentheses("(]"))      # False


'''
BFS 탐색
- 그래프에서 너비 우선 탐색을 통해 모든 노드를 방문하는 문제
- 큐를 사용해 가까운 노드부터 차례로 방문
'''

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            # print(node, end='')
            queue.extend(graph[node]-visited)

graph = {'A': {'B', 'C'}, 'B': {'A', 'D', 'E'}, 'C': {'A', 'F'}, 'D': {'B'}, 'E': {'B', 'F'}, 'F': {'C', 'E'}}
bfs(graph, 'A')  # A B C D E F

'''
두 수의 합 (해시맵 사용)
- 배열에서 두 수의 합이 특정 값이 되는 쌍을 찾는 문제
- 이미 본 숫자와의 합이 목표값이 되는지 해시맵을 이용해 빠르게 확인
'''

def two_sum(nums,target):
    hash_map = {}
    for i,num in enumerate(nums):
        compliement = target - num
        if compliement in hash_map:
            return hash_map[compliement], i
        hash_map[num]=i
    return []

print(two_sum([2, 7, 11, 15], 9))  # [0, 1]

# 향후 추가
# dfs 탐색 (재귀)
# 이진 트리 순회: 전위 중위 후위
# 참고 페이지: https://lincoding.tistory.com/107