import random

N, M, K = 300, 300, 10
print(N, M, K)
for _ in range(N):
    print(''.join([random.choice(['.','#']) for _ in range(M)]))

for _ in range(K):
    x, y = random.randint(1,N), random.randint(1,M)
    d_list = [random.randint(0,7) for _ in range(4)]
    print(x, y, *d_list)