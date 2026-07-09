class Node:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

def tinh_do_dai(head):
    dem = 0
    tam = head
    while tam is not None:
        dem += 1
        tam = tam.next
    return dem

def duyet_va_in(head):
    tam = head
    while tam is not None:
        print(tam.val, end=" ")
        tam = tam.next
    print()

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

print("Cac nut:", end=" ")
duyet_va_in(head)
print("Do dai:", tinh_do_dai(head))
