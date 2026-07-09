class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTableChaining:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        idx = self.hash_function(key)
        hien_tai = self.buckets[idx]
        while hien_tai:
            if hien_tai.key == key:
                hien_tai.value = value
                return
            hien_tai = hien_tai.next
        nut_moi = Node(key, value)
        nut_moi.next = self.buckets[idx]
        self.buckets[idx] = nut_moi

    def get(self, key):
        idx = self.hash_function(key)
        hien_tai = self.buckets[idx]
        while hien_tai:
            if hien_tai.key == key:
                return hien_tai.value
            hien_tai = hien_tai.next
        return None

    def remove(self, key):
        idx = self.hash_function(key)
        hien_tai = self.buckets[idx]
        truoc = None
        while hien_tai:
            if hien_tai.key == key:
                if truoc:
                    truoc.next = hien_tai.next
                else:
                    self.buckets[idx] = hien_tai.next
                return True
            truoc = hien_tai
            hien_tai = hien_tai.next
        return False

ht = HashTableChaining()
ht.put('a', 1)
print("Gia tri cua 'a':", ht.get('a'))
ht.remove('a')
print("Sau khi xoa 'a':", ht.get('a'))
