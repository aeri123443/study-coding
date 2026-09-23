'''
1차원 윷놀이
https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-yutnori-1d/description

문제 분석: 4m 20s
코드 작성: 13m 13s
최종 디버깅: 0m 0s

총 소요 시간: 17m 33s
'''

N, M, K = map(int, input().split())
cmds = list(map(int, input().split()))

horses = [0]*K
answer = 0

def bt(cnt):
    global answer

    if cnt == N:
        answer = max(answer, len([v for v in horses if v >= M-1]))
        return

    cmd = cmds[cnt]
    for h in range(K):
       horses[h] += cmd
       bt(cnt+1)
       horses[h] -= cmd

bt(0)
print(answer)