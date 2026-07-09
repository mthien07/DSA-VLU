class HashTableLazyDeletion:
    def __init__(self, size=5):
        self.size = size
        self.keys = [None] * size
        self.DELETED = "DELETED"

    def put(self, key):
        idx = key % self.size
        while self.keys[idx] is not None and self.keys[idx] != self.DELETED:
            idx = (idx + 1) % self.size
        self.keys[idx] = key

    def remove(self, key):
        idx = key % self.size
        diem_bat_dau = idx
        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                self.keys[idx] = self.DELETED
                return
            idx = (idx + 1) % self.size
            if idx == diem_bat_dau:
                break

ht = HashTableLazyDeletion()
ht.put(1)
ht.put(6)
ht.remove(1)
print("Trang thai bang:", ht.keys)
