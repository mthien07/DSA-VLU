class Node:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

def co_chu_trinh(head):
    rua = head
    tho = head
    while tho is not None and tho.next is not None:
        rua = rua.next
        tho = tho.next.next
        if rua == tho:
            return True
    return False

head = Node(1)
nut2 = Node(2)
nut3 = Node(3)
head.next = nut2
nut2.next = nut3
nut3.next = nut2

print("Co chu trinh khong?", co_chu_trinh(head))
