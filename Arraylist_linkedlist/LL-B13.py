class Node:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

def lay_giua(head):
    if head is None: return head
    cham = head
    nhanh = head.next
    while nhanh is not None and nhanh.next is not None:
        cham = cham.next
        nhanh = nhanh.next.next
    return cham

def tron_hai_list(l1, l2):
    tam = Node()
    ht = tam
    while l1 and l2:
        if l1.val < l2.val:
            ht.next = l1
            l1 = l1.next
        else:
            ht.next = l2
            l2 = l2.next
        ht = ht.next
    if l1: ht.next = l1
    if l2: ht.next = l2
    return tam.next

def merge_sort(head):
    if head is None or head.next is None:
        return head
    giua = lay_giua(head)
    ke_tiep = giua.next
    giua.next = None
    
    trai = merge_sort(head)
    phai = merge_sort(ke_tiep)
    return tron_hai_list(trai, phai)

def in_list(head):
    tam = head
    while tam:
        print(tam.val, end="->")
        tam = tam.next
    print("null")

h = Node(3, Node(1, Node(2)))
print("Truoc:")
in_list(h)
print("Sau:")
in_list(merge_sort(h))
