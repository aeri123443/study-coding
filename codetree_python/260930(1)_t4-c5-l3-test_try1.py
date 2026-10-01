'''
알바로 부자 되기
https://www.codetree.ai/ko/trails/complete/curated-cards/test-being-rich-by-working-part-time/description
'''

N = int(input())
dp_s = [-1]
dp_e = [0]
dp_p = [0]

answer = 0
for _ in range(N):
    s, e, p = map(int, input().split())

    max_pay = 0
    for i in range(len(dp_p)):
        if dp_e[i] < s:
            max_pay = max(max_pay, dp_p[i])
    dp_s.append(s)
    dp_e.append(e)
    dp_p.append(max_pay+p)
    answer = max(answer, max_pay+p)

print(answer)
