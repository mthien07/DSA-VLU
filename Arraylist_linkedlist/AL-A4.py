class ArrayList:
    def __init__(self):
        self.items = []
        
    def append(self, val):
        self.items.append(val)

    def indexOf(self, val):
        for i in range(len(self.items)):
            if self.items[i] == val:
                return i
        return -1

al = ArrayList()
al.append(5); al.append(3); al.append(7)
print("Mang:", al.items)
print("Tim so 7:", al.indexOf(7))
print("Tim so 10:", al.indexOf(10))
