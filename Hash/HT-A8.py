class HashTableDoubleHashing:
    def __init__(self, size=7):
        self.size = size
        self.table = [None] * size

    def h1(self, key):
        return key % self.size

    def h2(self, key):
        return 5 - (key % 5)

    def put(self, key):
        idx = self.h1(key)
        buoc_do = self.h2(key)
        i = 0
        while self.table[(idx + i * buoc_do) % self.size] is not None:
            i += 1
            if i == self.size:
                print("Bang day!")
                return
        self.table[(idx + i * buoc_do) % self.size] = key

ht = HashTableDoubleHashing()
ht.put(10)
ht.put(17)
print("Bang sau khi them:", ht.table)
