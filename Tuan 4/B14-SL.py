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

def selection_sort_linked_list(head):
    sorted_head = None
    sorted_tail = None
    while head:
        # Tim node nho nhat
        min_node = head
        prev_min = None
        current = head
        prev = None
        while current:
            if current.data < min_node.data:
                min_node = current
                prev_min = prev
            prev = current
            current = current.next
        # Go min_node ra khoi danh sach
        if prev_min:
            prev_min.next = min_node.next
        else:
            head = min_node.next
        # Noi vao cuoi danh sach sorted
        min_node.next = None
        if sorted_head is None:
            sorted_head = min_node
            sorted_tail = min_node
        else:
            sorted_tail.next = min_node
            sorted_tail = min_node
    return sorted_head
