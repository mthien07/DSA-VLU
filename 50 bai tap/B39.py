class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def nut_bat_dau_chu_trinh(head):
    rua = head
    tho = head
    co_chu_trinh = False
    
    while tho and tho.next:
        rua = rua.next
        tho = tho.next.next
        
        if rua == tho:
            co_chu_trinh = True
            break
            
    if not co_chu_trinh:
        return None
        
    rua = head
    while rua != tho:
        rua = rua.next
        tho = tho.next
        
    return rua

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.next = n2
n2.next = n3
n3.next = n2

nut = nut_bat_dau_chu_trinh(n1)
print(f"Nut bat dau chu trinh: {nut.val if nut else None}")
