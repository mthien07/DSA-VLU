class HashTableRehash:
    def __init__(self, size=4):
        self.size = size
        self.count = 0
        self.keys = [None] * size
        self.values = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def rehash(self):
        print(f"Rehashing: Tang kich thuoc tu {self.size} len {self.size * 2}")
        old_keys = self.keys
        old_values = self.values
        self.size *= 2
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self.count = 0
        for i in range(len(old_keys)):
            if old_keys[i] is not None:
                self.put(old_keys[i], old_values[i])

    def put(self, key, value):
        if self.count / self.size > 0.75:
            self.rehash()
        idx = self.hash_function(key)
        while self.keys[idx] is not None and self.keys[idx] != key:
            idx = (idx + 1) % self.size
        if self.keys[idx] is None:
            self.count += 1
        self.keys[idx] = key
        self.values[idx] = value

ht = HashTableRehash()
ht.put(1, "A")
ht.put(2, "B")
ht.put(3, "C")
ht.put(4, "D")
print("Hoan thanh.")
