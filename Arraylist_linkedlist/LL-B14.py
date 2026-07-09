class Node:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

def cong_hai_so(l1, l2):
    tam = Node(0)
    hien_tai = tam
    nho = 0
    
    while l1 is not None or l2 is not None or nho > 0:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        tong = val1 + val2 + nho
        
        nho = tong // 10
        hien_tai.next = Node(tong % 10)
        hien_tai = hien_tai.next
        
        if l1: l1 = l1.next
        if l2: l2 = l2.next
        
    return tam.next

def in_list(head):
    tam = head
    while tam:
        print(tam.val, end="")
        tam = tam.next
    print()

l1 = Node(2, Node(4, Node(3)))
l2 = Node(5, Node(6, Node(4)))

kq = cong_hai_so(l1, l2)
print("243 + 564 dang luu nguoc (342 + 465) =")
in_list(kq)
