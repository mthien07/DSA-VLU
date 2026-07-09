class Node:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

def dao_nguoc(head):
    truoc = None
    hien_tai = head
    
    while hien_tai is not None:
        sau = hien_tai.next
        hien_tai.next = truoc
        truoc = hien_tai
        hien_tai = sau
        
    return truoc

def in_list(head):
    tam = head
    while tam:
        print(tam.val, end="->")
        tam = tam.next
    print("null")

head = Node(1, Node(2, Node(3)))
print("Truoc dao:")
in_list(head)
head_moi = dao_nguoc(head)
print("Sau dao:")
in_list(head_moi)
