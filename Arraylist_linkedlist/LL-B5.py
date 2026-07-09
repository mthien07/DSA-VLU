class Node:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

def xoa_nut(head, x):
    if head is not None and head.val == x:
        return head.next
        
    tam = head
    while tam is not None and tam.next is not None:
        if tam.next.val == x:
            tam.next = tam.next.next
            return head
        tam = tam.next
    return head

def in_list(head):
    tam = head
    while tam:
        print(tam.val, end="->")
        tam = tam.next
    print("null")

head = Node(1, Node(2, Node(3, Node(2))))
print("Truoc xoa 2:")
in_list(head)
head = xoa_nut(head, 2)
print("Sau xoa 2 dau tien:")
in_list(head)
