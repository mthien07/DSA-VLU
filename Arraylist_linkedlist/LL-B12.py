class Node:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

def tim_bat_dau_chu_trinh(head):
    rua = head
    tho = head
    while tho is not None and tho.next is not None:
        rua = rua.next
        tho = tho.next.next
        if rua == tho:
            rua = head
            while rua != tho:
                rua = rua.next
                tho = tho.next
            return rua
    return None

h = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
h.next = n2; n2.next = n3; n3.next = n4; n4.next = n2

diem = tim_bat_dau_chu_trinh(h)
if diem:
    print("Diem bat dau chu trinh la:", diem.val)
else:
    print("Khong co chu trinh")
