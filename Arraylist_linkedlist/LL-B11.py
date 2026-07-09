class DNode:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def pushBack(self, val):
        nut_moi = DNode(val)
        if self.head is None:
            self.head = self.tail = nut_moi
            return
        self.tail.next = nut_moi
        nut_moi.prev = self.tail
        self.tail = nut_moi

    def in_xuoi(self):
        tam = self.head
        while tam:
            print(tam.val, end=" <-> ")
            tam = tam.next
        print("null")

    def in_nguoc(self):
        tam = self.tail
        while tam:
            print(tam.val, end=" <-> ")
            tam = tam.prev
        print("null")

dll = DoublyLinkedList()
dll.pushBack(1); dll.pushBack(2); dll.pushBack(3)
print("Xuoi:")
dll.in_xuoi()
print("Nguoc:")
dll.in_nguoc()
