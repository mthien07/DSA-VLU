class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(head):
    result = []
    while head:
        result.append(str(head.data))
        head = head.next
    print(" -> ".join(result) + " -> null")

def insertion_sort_linked_list(head):
    sorted_head = None
    current = head
    while current:
        next_node = current.next
        # Chen current vao danh sach sorted
        if sorted_head is None or sorted_head.data >= current.data:
            current.next = sorted_head
            sorted_head = current
        else:
            temp = sorted_head
            while temp.next and temp.next.data < current.data:
                temp = temp.next
            current.next = temp.next
            temp.next = current
        current = next_node
    return sorted_head
