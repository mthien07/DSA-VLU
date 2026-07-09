class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def gop_danh_sach(l1, l2):
    dummy = Node(0)
    hien_tai = dummy
    
    while l1 and l2:
        if l1.val <= l2.val:
            hien_tai.next = l1
            l1 = l1.next
        else:
            hien_tai.next = l2
            l2 = l2.next
        hien_tai = hien_tai.next
        
    if l1:
        hien_tai.next = l1
    if l2:
        hien_tai.next = l2
        
    return dummy.next

def in_danh_sach(head):
    ket_qua = []
    while head:
        ket_qua.append(str(head.val))
        head = head.next
    print(" -> ".join(ket_qua))

l1 = Node(1, Node(3))
l2 = Node(2, Node(4))
l_gop = gop_danh_sach(l1, l2)
in_danh_sach(l_gop)
