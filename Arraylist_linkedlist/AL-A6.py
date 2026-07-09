class DynamicArray:
    def __init__(self, capacity=4):
        self.capacity = capacity
        self.size = 0
        self.items = [None] * self.capacity
        
    def append(self, val):
        if self.size == self.capacity:
            self.capacity *= 2
            mang_moi = [None] * self.capacity
            for i in range(self.size):
                mang_moi[i] = self.items[i]
            self.items = mang_moi
            print("=> Da cap phat mang moi cap=", self.capacity)
            
        self.items[self.size] = val
        self.size += 1

arr = DynamicArray(4)
for i in range(5):
    arr.append(i + 1)
print("Mang hien tai (size:", arr.size, ", capacity:", arr.capacity, ") ->", arr.items[:arr.size])
