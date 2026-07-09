class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def co_chu_trinh(head):
    
    rua = head
    tho = head
    
    while tho and tho.next:
        rua = rua.next
        tho = tho.next.next
        
        if rua == tho:
            return True
            
    return False

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.next = n2
n2.next = n3
n3.next = n1

print(f"Co chu trinh: {co_chu_trinh(n1)}")
