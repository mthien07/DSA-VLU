class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def dao_nguoc_danh_sach(head):
    truoc_do = None
    hien_tai = head
    
    while hien_tai:
        tam = hien_tai.next
        hien_tai.next = truoc_do
        truoc_do = hien_tai
        hien_tai = tam
        
    return truoc_do

def in_danh_sach(head):
    ket_qua = []
    while head:
        ket_qua.append(str(head.val))
        head = head.next
    print(" -> ".join(ket_qua))

head = Node(1, Node(2, Node(3)))
print("Truoc khi dao nguoc:")
in_danh_sach(head)

head_moi = dao_nguoc_danh_sach(head)
print("Sau khi dao nguoc:")
in_danh_sach(head_moi)
