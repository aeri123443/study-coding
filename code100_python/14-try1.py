'''
p.180 14. 표 편집
https://school.programmers.co.kr/learn/courses/30/lessons/81303
소요시간: 97m 14s
'''

def solution(n, k, cmd):
    global mem, u, d, p, z_stack
    mem = ['O']*(n+2)
    z_stack = []
    u = [i-1 for i in range(n+2)]
    d = [i+1 for i in range(n+2)]
    p = k+1

    def up(x):
        global mem, u, d, p
        for _ in range(x):
            if u[p]>=0:
                p = u[p]
            else: 
                break
    def down(x):
        global mem, u, d, p
        for _ in range(x):
            if d[p]<n+1:
                p = d[p]
            else: 
                break
    def cancel():
        global mem, u, d, p, z_stack
        mem[p] = 'X'
        z_stack.append(p)
        u[d[p]]=u[p]
        d[u[p]]=d[p]
        if d[p]<n+1:
            down(1)
        else: 
            up(1)
    def undo():
        global mem, u, d, p, z_stack
        last_undo = z_stack.pop()
        u[d[last_undo]]=last_undo
        d[u[last_undo]]=last_undo
        mem[last_undo]='O'
    
    for item in cmd:
        if item[0]=='U':
            up(int(item.split()[1]))
        elif item[0]=='D':
            down(int(item.split()[1]))
        elif item[0]=='C':
            cancel()
        elif item[0]=='Z':
            undo()

        # print()
        # print('cmd', item)
        # print('mem', mem)
        # print('u', u)
        # print('d', d)
        # print('p', p)
        # print('z_stack', z_stack)
        
    return ''.join(mem[1:(len(mem)-1)])

# OOOOXOOO
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
)# OOXOXOOO
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))