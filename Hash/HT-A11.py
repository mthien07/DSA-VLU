class HashSet:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def add(self, key):
        idx = self.hash_function(key)
        if key not in self.buckets[idx]:
            self.buckets[idx].append(key)

    def contains(self, key):
        idx = self.hash_function(key)
        return key in self.buckets[idx]

    def remove(self, key):
        idx = self.hash_function(key)
        if key in self.buckets[idx]:
            self.buckets[idx].remove(key)

hs = HashSet()
hs.add(1)
hs.add(1)
hs.add(2)
print("Contains 1:", hs.contains(1))
print("Buckets hien tai:", hs.buckets)
