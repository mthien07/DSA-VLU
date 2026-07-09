class Node:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

def tim_nut_giua(head):
    cham = head
    nhanh = head
    while nhanh is not None and nhanh.next is not None:
        cham = cham.next
        nhanh = nhanh.next.next
    if cham is None: return None
    return cham.val

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print("Nut giua cua 1->2->3->4->5 la:", tim_nut_giua(head))
