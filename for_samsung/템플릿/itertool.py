# 순열
def permutation(arr, r):
    result = []
    path = []
    used = [False]*len(arr)

    def dfs():
        if len(path) == r:
            result.append(path[:])
            return
        for i in range(len(arr)):
            if used[i]:
                continue
            used[i] = True
            path.append(arr[i])
            dfs()
            used[i] = False
            path.pop()

    dfs()
    return result

# 조합
def combination(arr, r):
    result = []
    path = []

    def dfs(start):
        if len(path) == r:
            result.append(path[:])
            return

        for i in range(start, len(arr)):
            path.append(arr[i])
            dfs(i+1)
            path.pop()

    dfs(0)
    return result

# 중복 순열
def product(arr, r):
    result = []
    path = []

    def dfs():
        if len(path) == r:
            result.append(path[:])
            return
        for i in range(len(arr)):
            path.append(arr[i])
            dfs()
            path.pop()

    dfs()
    return result

# 중복 조합
def combinations_with_replacement(arr, r):
    result = []
    path = []

    def dfs(start):
        if len(path)==r:
            result.append(path[:])
            return

        for i in range(start, len(arr)):
            path.append(arr[i])
            dfs(i)
            path.pop()

    dfs(0)
    return result
arr = [1,2,3]
r = 2

print('순열: ', len(permutation(arr, r)), permutation(arr, r) )
print('조합: ', len(combination(arr, r)), combination(arr, r) )
print('중복순열: ', len(product(arr, r) ), product(arr, r) )
print('중복조합: ', len(combinations_with_replacement(arr, r)), combinations_with_replacement(arr, r) )
