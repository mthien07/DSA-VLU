class Node:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None

    def pushFront(self, val):
        nut_moi = Node(val)
        nut_moi.next = self.head
        self.head = nut_moi

    def pushBack(self, val):
        nut_moi = Node(val)
        if self.head is None:
            self.head = nut_moi
            return
        
        tam = self.head
        while tam.next is not None:
            tam = tam.next
        tam.next = nut_moi

    def display(self):
        tam = self.head
        while tam is not None:
            print(tam.val, end=" -> ")
            tam = tam.next
        print("null")

ll = LinkedList()
ll.pushFront(2)
ll.pushBack(5)
ll.display()
