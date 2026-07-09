class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def tim_diem_giua(head):
    rua = head
    tho = head
    
    while tho and tho.next:
        rua = rua.next
        tho = tho.next.next
        
    return rua

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
giua = tim_diem_giua(head)
print(f"Diem giua la: {giua.val if giua else None}")
