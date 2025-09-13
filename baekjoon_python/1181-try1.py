'''
1181. 단어 정렬
https://www.acmicpc.net/problem/1181
'''

N = int(input())
arr = list({input() for _ in range(N)})
arr.sort()
arr.sort(key=lambda x:len(x))
print(*arr, sep='\n')