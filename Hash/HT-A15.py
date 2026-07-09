import hashlib

def hash_string(s):
    return int(hashlib.md5(s.encode()).hexdigest(), 16)

class ConsistentHashing:
    def __init__(self, num_replicas=3):
        self.num_replicas = num_replicas
        self.ring = {}
        self.sorted_keys = []

    def add_node(self, node_name):
        for i in range(self.num_replicas):
            key = hash_string(f"{node_name}_{i}")
            self.ring[key] = node_name
            self.sorted_keys.append(key)
        self.sorted_keys.sort()

    def get_node(self, key_name):
        if not self.ring:
            return None
        hash_val = hash_string(key_name)
        for key in self.sorted_keys:
            if hash_val <= key:
                return self.ring[key]
        return self.ring[self.sorted_keys[0]]

ch = ConsistentHashing()
ch.add_node("Server_A")
ch.add_node("Server_B")
print("Key 'my_file.txt' duoc luu o:", ch.get_node("my_file.txt"))
