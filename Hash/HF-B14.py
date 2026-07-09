class BloomFilter:
    def __init__(self, size=100, num_hashes=3):
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = [0] * size

    def _hashes(self, item):
        hashes = []
        for i in range(self.num_hashes):
            h = hash(str(item) + str(i)) % self.size
            hashes.append(h)
        return hashes

    def add(self, item):
        for h in self._hashes(item):
            self.bit_array[h] = 1

    def contains(self, item):
        for h in self._hashes(item):
            if self.bit_array[h] == 0:
                return False
        return True

bf = BloomFilter()
bf.add("apple")
print("Chua 'apple':", bf.contains("apple"))
print("Chua 'banana':", bf.contains("banana"))
