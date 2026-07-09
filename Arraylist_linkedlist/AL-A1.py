class ArrayList:
    def __init__(self):
        self.items = []
    def add(self, val):
        self.items.append(val)
    def get(self, index):
        if index < 0 or index >= len(self.items):
            print("sai roi m")
            return None
        return self.items[index]

    def set(self, index, val):
        if index < 0 or index >= len(self.items):
            print("sai roi m")
            return
        self.items[index] = val
    def getSize(self):
        return len(self.items)
    def display(self):
        print("ArrayList:", self.items)

al = ArrayList()
al.add(1)
al.add(2)
al.add(3)
al.display()
print("Phan tu tai index 1:", al.get(1))
