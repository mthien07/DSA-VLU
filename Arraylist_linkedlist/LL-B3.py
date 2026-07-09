class Node:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

def tim_kiem(head, gia_tri):
    vi_tri = 0
    tam = head
    while tam is not None:
        if tam.val == gia_tri:
            return vi_tri
        tam = tam.next
        vi_tri += 1
    return -1

head = Node(1, Node(2, Node(3)))
print("Tim 2 -> vi tri:", tim_kiem(head, 2))
print("Tim 5 -> vi tri:", tim_kiem(head, 5))
