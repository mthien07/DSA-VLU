class Node:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

def chen_sau_nut(nut_truoc, val):
    if nut_truoc is None:
        return
    nut_moi = Node(val)
    nut_moi.next = nut_truoc.next
    nut_truoc.next = nut_moi

def in_list(head):
    tam = head
    while tam:
        print(tam.val, end="->")
        tam = tam.next
    print("null")

head = Node(1, Node(3))
print("Truoc khi chen:")
in_list(head)

chen_sau_nut(head, 2)
print("Sau khi chen:")
in_list(head)
