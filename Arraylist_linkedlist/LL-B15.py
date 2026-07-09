class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def xoa_nut(self, nut):
        truoc = nut.prev
        sau = nut.next
        truoc.next = sau
        sau.prev = truoc

    def them_len_dau(self, nut):
        sau_head = self.head.next
        self.head.next = nut
        nut.prev = self.head
        nut.next = sau_head
        sau_head.prev = nut

    def get(self, key):
        if key in self.dict:
            nut = self.dict[key]
            self.xoa_nut(nut)
            self.them_len_dau(nut)
            return nut.val
        return -1

    def put(self, key, value):
        if key in self.dict:
            nut = self.dict[key]
            self.xoa_nut(nut)
            nut.val = value
            self.them_len_dau(nut)
        else:
            if len(self.dict) >= self.capacity:
                nut_cuoi = self.tail.prev
                self.xoa_nut(nut_cuoi)
                del self.dict[nut_cuoi.key]
            nut_moi = Node(key, value)
            self.dict[key] = nut_moi
            self.them_len_dau(nut_moi)

cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print("Get 1:", cache.get(1))
cache.put(3, 3)
print("Get 2:", cache.get(2))
