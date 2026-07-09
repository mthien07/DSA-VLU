class Node:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

def tron_danh_sach(head1, head2):
    nut_tam = Node(0)
    hien_tai = nut_tam
    
    while head1 is not None and head2 is not None:
        if head1.val < head2.val:
            hien_tai.next = head1
            head1 = head1.next
        else:
            hien_tai.next = head2
            head2 = head2.next
        hien_tai = hien_tai.next
        
    if head1 is not None:
        hien_tai.next = head1
    if head2 is not None:
        hien_tai.next = head2
        
    return nut_tam.next

def in_list(head):
    tam = head
    while tam:
        print(tam.val, end="->")
        tam = tam.next
    print("null")

h1 = Node(1, Node(3, Node(5)))
h2 = Node(2, Node(4))
kq = tron_danh_sach(h1, h2)
print("Sau khi tron:")
in_list(kq)
