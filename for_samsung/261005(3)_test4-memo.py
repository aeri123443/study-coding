import random
import sys

sys.stdout = open("/Users/jeong-aeli/Desktop/employment/study-coding/input.txt", "w", encoding="utf-8")

N = 200
Q = 200

def make_arr():
    arr = []
    for _ in range(N):
        l = [random.randint(0,255) for _ in range(N)]
        l = ' '.join(map(str, l))
        arr.append(l)
    return '\n'.join(arr)

a = make_arr()
b = make_arr()
c = make_arr()

print(N)
print(a)
print(b)
print(c)

line = []
for _ in range(Q):
    cmd = random.randint(1,2)
    if cmd == 1:
        x, y, c = random.randint(1,N), random.randint(1,N), random.randint(1,2*N)
        line.append(f'100 {x} {y} {c}')
    else:
        c = random.choice(['R', 'G', 'B', 'W'])
        line.append(f'200 {c}')


print(Q)
print('\n'.join(line))

print()

sys.stdout.close()
