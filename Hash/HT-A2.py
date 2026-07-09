class HashTableLinearProbing:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        idx = self.hash_function(key)
        diem_bat_dau = idx
        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                self.values[idx] = value
                return
            idx = (idx + 1) % self.size
            if idx == diem_bat_dau:
                print("Loi: Bang bam da day!")
                return
        self.keys[idx] = key
        self.values[idx] = value

    def get(self, key):
        idx = self.hash_function(key)
        diem_bat_dau = idx
        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                return self.values[idx]
            idx = (idx + 1) % self.size
            if idx == diem_bat_dau:
                break
        return None

ht = HashTableLinearProbing()
ht.put('a', 1)
ht.put('k', 2)
print("Gia tri cua 'a':", ht.get('a'))
print("Gia tri cua 'k':", ht.get('k'))
