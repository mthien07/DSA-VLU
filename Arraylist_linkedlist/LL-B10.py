class Node:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

def xoa_nut_k_tu_cuoi(head, k):
    nut_tam = Node(0)
    nut_tam.next = head
    nhanh = nut_tam
    cham = nut_tam
    
    for i in range(k + 1):
        if nhanh is None: return head
        nhanh = nhanh.next
        
    while nhanh is not None:
        nhanh = nhanh.next
        cham = cham.next
        
    cham.next = cham.next.next
    return nut_tam.next

def in_list(head):
    tam = head
    while tam:
        print(tam.val, end="->")
        tam = tam.next
    print("null")

h = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print("Xoa 4 (vi tri k=2 tu cuoi):")
h = xoa_nut_k_tu_cuoi(h, 2)
in_list(h)
