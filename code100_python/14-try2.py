'''
p.180 14. 표 편집
https://school.programmers.co.kr/learn/courses/30/lessons/81303
try2: 연결리스트 활용해보기
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self, n, k):
        self.root = Node(0)
        self.current = self.root
        self.trash = []

        # 0~n-1까지 연결하기
        temp = self.root
        for i in range(n):
            new_node = Node(i)
            # 포인터 지정
            if i==k:
                self.current = new_node
            if i==0: continue
            temp.next = new_node
            new_node.prev = temp
            temp = temp.next

    def up(self, x):
        for _ in range(x):
            if self.current.prev:
                self.current = self.current.prev
            else:
                break
    
    def down(self, x):
        for _ in range(x):
            if self.current.next:
                self.current = self.current.next
            else:
                break

    def remove(self):
        deleted_node = self.current
        if deleted_node.prev:
            deleted_node.prev.next = deleted_node.next
        else:
            self.root = deleted_node.next
        ## review: if deleted_node.next가 두 번 있음... 합쳐도 될듯
        if deleted_node.next:
            deleted_node.next.prev = deleted_node.prev
        self.trash.append(deleted_node)
        if deleted_node.next:
            self.current = deleted_node.next
        else:
            self.current = deleted_node.prev
    
    def undo(self):
        undo_node = self.trash.pop()
        if undo_node.prev:
            undo_node.prev.next = undo_node
        else:
            self.root = undo_node
        if undo_node.next:
            undo_node.next.prev = undo_node
        
def solution(n, k, cmd):
    linked_list = LinkedList(n, k)

    for c in cmd:
        if c[0]=='U':
            linked_list.up( int(c.split()[1]))
        elif c[0]=='D':
            linked_list.down( int(c.split()[1]))
        elif c[0]=='C':
            linked_list.remove()
        elif c[0]=='Z':
            linked_list.undo()
        # print('c', c)
        # print('p', linked_list.current.data)
        # print()

    ## 이것보단 ['X']*n이 더 효율적
    answer = ['X' for _ in range(n)]

    temp = linked_list.root
    ## while temp로 처리했으면 더 좋았을듯
    while(True):
        answer[temp.data] = 'O'
        if temp.next:
            temp = temp.next
        else:
            break
    return ''.join(answer)

# OOOOXOOO
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
# OOXOXOOO
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))